import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 120:
        return 0
    max_r = rows
    max_c = cols
    valid_submatrices = 0
    for r in range(1, max_r + 1):
        for c in range(1, max_c + 1):
            if r * c == 120:
                submatrix_count = (max_r - r + 1) * (max_c - c + 1)
                valid_submatrices += submatrix_count
    return valid_submatrices