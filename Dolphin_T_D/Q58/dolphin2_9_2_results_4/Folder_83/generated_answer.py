import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            if matrix[i][j] == 47:
                count += 1
            if matrix[i][j + 1] == 47:
                count += 1
            if matrix[i + 1][j] == 47:
                count += 1
            if matrix[i + 1][j + 1] == 47:
                count += 1
    return count