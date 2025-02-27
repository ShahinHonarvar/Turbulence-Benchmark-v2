from numpy import *

def submatrix_with_particular_sum(matrix):
    return list(where(sum(matrix, axis=1) == -86))