import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for row_length in range(1, matrix.shape[0] - row + 1):
                for col_length in range(1, matrix.shape[1] - col + 1):
                    submatrix = matrix[row:row + row_length, col:col + col_length]
                    if np.sum(submatrix) == -57:
                        submatrices.append(submatrix)
    return submatrices