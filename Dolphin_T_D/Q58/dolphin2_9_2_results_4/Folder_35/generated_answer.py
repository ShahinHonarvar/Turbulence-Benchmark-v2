import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 1 and (i > 0 and j > 0):
                if matrix[i - 1][j] == 1 and matrix[i][j - 1] == 1 and (matrix[i - 1][j - 1] == 1):
                    submatrix_count += 1
    return submatrix_count