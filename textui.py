# Text-Based User Interface
# Interface of game
#
# Copyright 2011, Zhao Zhang, RuiZhou Min
# All rights reserved.
#
# Created:		Zhao Zhang (zz9@ualberta.ca) RuiZhou Min

# Imports
import game

# Functions

class Interface(game.ReversiGameLogic):
    def drawBoard(self):
        FIRST="  1 2 3 4 5 6 7 8"
        ORDER=['A','B','C','D','E','F','G','H']
        print(FIRST)
        x=0
        for i in ORDER:
            print(i,self.board[x][0],self.board[x][1],self.board[x][2],self.board[x][3],self.board[x][4],self.board[x][5],self.board[x][6],self.board[x][7])
            x=x+1    
#draw a new board            
            
    def getPlayerMove(self):
        DIGIT = '1 2 3 4 5 6 7 8'.split()
        ORDER_MOVE={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
        while True:
            print("Enter move (or 'help'):")
            move = input().upper()
            if move == 'HELP':
                print('The user can enter a move that is applicable to the current board.')
                print('The first character of the move refers to the row.')
                print('It can be entered in either lower or upper case.')
                print('The second character refers to the column')
                print('The game ends when neither player can make a move.')
                print('In addition, the user can enter help.')
            elif len(move)==2 and (move[0] in ORDER_MOVE) and (move[1] in DIGIT):
                x = int(ORDER_MOVE[move[0]])-1
                y = int(move[1])-1
                if self.isValidMove(x,y) == False:
                    continue
                else:
                    break
            else:
                print("That is not a valid move.")
        return [x,y]
#user's inferface(move or help)
    
    def printValid(self):
        ORDER={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}
        printValid=[]
        for x in range(8):
            for y in range(8):
                if self.isValidMove(x, y)!=False:
                    printValid.append(ORDER[x+1]+str(y+1)+', ')
        count=1
        while count < len(printValid):
            printValid[0] = printValid[0] + printValid[count]
            count += 1
        print('Legal Moves: ',printValid[0])

#print legal moves