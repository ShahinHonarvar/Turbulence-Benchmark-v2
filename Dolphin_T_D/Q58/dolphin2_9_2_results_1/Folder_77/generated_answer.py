import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    height, width = matrix.shape
    for i in range(height - 1):
        for j in range(width - 1):
            if sum(matrix[i:i + 2, j:j + 2]) == 179:
                submatrix_count += 1
    return submatrix_count