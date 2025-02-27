import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 28
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == submatrix_size:
                submatrix_count += (rows - r + 1) * (cols - c + 1)
    return submatrix_count