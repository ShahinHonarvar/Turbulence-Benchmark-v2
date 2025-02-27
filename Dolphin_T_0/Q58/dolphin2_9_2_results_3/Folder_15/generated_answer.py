import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 2
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == 1 and matrix[i][j - 1] == 1 and (matrix[i - 1][j] == 1):
                count += 1
    return count