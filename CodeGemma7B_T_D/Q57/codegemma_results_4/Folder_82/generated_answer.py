from numpy import *

def submatrix_with_particular_sum(matrix):
    matrix_size = matrix.shape[0] * matrix.shape[1]
    for i in range(matrix_size):
        for j in range(i + 1, matrix_size):
            submatrix = matrix.flatten()[i:j + 1]
            if sum(submatrix) == -27:
                return submatrix.reshape(matrix.shape[0], matrix.shape[1])
    return []