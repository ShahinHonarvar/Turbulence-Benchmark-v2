import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 3 or cols < 3:
        return 0
    return (rows - 2) * (cols - 2)