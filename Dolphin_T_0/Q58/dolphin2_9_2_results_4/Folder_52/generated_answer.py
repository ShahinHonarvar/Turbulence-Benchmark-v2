import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            s = matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j]
            s += matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1]
            s += matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2]
            if s == 147:
                count += 1
    return count