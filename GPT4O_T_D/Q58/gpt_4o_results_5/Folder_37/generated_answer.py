import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    if rows * cols < 64:
        return 0
    if rows >= 8 and cols >= 8:
        max_submatrices = (rows - 7) * (cols - 7)
        return max_submatrices
    return 0