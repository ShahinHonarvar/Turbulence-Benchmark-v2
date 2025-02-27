import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for row_len in range(row, matrix.shape[0] + 1):
                for col_len in range(col, matrix.shape[1] + 1):
                    submatrix = matrix[row:row_len, col:col_len]
                    if np.sum(submatrix) == -83:
                        submatrices.append(submatrix)
    return submatrices