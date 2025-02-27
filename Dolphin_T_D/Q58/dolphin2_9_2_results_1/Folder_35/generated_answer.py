import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if matrix[i][j] == matrix[i + 1][j] == matrix[i + 2][j] == matrix[i][j + 1] == matrix[i + 1][j + 1] == matrix[i + 2][j + 1] == matrix[i][j + 2] == matrix[i + 1][j + 2] == matrix[i + 2][j + 2] == 1:
                count += 1
    return count