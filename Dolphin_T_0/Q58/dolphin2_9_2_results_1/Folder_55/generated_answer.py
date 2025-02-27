import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            if matrix[i:i + 6, j:j + 6].size == 39:
                count += 1
    return count