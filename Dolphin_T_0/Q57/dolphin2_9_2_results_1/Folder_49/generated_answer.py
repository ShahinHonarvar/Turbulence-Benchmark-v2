import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    row_num, col_num = matrix.shape
    submatrices = []
    for i1 in range(row_num):
        for j1 in range(col_num):
            for i2 in range(i1, row_num):
                for j2 in range(j1, col_num):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == -42:
                        submatrices.append(submatrix)
    return submatrices