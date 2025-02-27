import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 1):
        for j in range(width - 1):
            if matrix[i, j] == 4:
                count += 1
            if matrix[i, j + 1] == 4:
                count += 1
            if matrix[i + 1, j] == 4:
                count += 1
            if matrix[i + 1, j + 1] == 4:
                count += 1
    return count