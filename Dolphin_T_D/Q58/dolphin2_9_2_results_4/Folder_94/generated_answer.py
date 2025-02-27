import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            if matrix[i, j] == 93 and matrix[i, j + 1] == 93 and (matrix[i, j + 2] == 93) and (matrix[i + 1, j] == 93) and (matrix[i + 1, j + 1] == 93) and (matrix[i + 1, j + 2] == 93) and (matrix[i + 2, j] == 93) and (matrix[i + 2, j + 1] == 93) and (matrix[i + 2, j + 2] == 93):
                count += 1
    return count