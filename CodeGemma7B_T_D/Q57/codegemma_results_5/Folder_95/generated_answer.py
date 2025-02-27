from numpy import *

def submatrix_with_particular_sum(matrix):
    """
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 19:
                return [[matrix[i][j]]]
    return []