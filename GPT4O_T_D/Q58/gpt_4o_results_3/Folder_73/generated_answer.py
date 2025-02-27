import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    num_submatrices = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r * c == 41:
                num_submatrices += (rows - r + 1) * (cols - c + 1)
    return num_submatrices