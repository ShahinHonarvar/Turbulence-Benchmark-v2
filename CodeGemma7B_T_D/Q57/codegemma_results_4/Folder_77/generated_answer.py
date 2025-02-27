from numpy import *

def submatrix_with_particular_sum(matrix):
    return [submat for submat in matrix if sum(flatten(submat)) == -336]