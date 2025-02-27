import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 4):
        for j in range(cols - 4):
            if matrix[i, j] + matrix[i, j + 1] + matrix[i, j + 2] + matrix[i, j + 3] + matrix[i + 1, j] + matrix[i + 1, j + 1] + matrix[i + 1, j + 2] + matrix[i + 1, j + 3] + matrix[i + 2, j] + matrix[i + 2, j + 1] + matrix[i + 2, j + 2] + matrix[i + 2, j + 3] + matrix[i + 3, j] + matrix[i + 3, j + 1] + matrix[i + 3, j + 2] + matrix[i + 3, j + 3] == 16:
                count += 1
    return count