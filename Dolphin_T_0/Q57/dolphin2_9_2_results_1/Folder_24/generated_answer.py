import numpy as np
from numpy.lib.arraysetops import isin

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_size = len(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            for row_end in range(i, matrix_size):
                for col_end in range(j, matrix_size):
                    submatrix = matrix[i:row_end + 1, j:col_end + 1]
                    if np.sum(submatrix) == -36:
                        submatrices.append(submatrix)
    return submatrices