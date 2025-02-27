import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 2 or cols < 2:
        return 0
    count = (rows - 1) * (cols - 1)
    return count