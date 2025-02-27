import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 4 or cols < 4:
        return 0
    return (rows - 3) * (cols - 3)