import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 34
    total_count = 0
    height, width = matrix.shape
    for i in range(height - n + 1):
        for j in range(width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.sum() == n * 34:
                total_count += 1
    return total_count