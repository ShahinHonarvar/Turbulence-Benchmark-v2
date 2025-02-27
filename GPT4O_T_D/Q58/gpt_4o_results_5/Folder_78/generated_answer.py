import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    return max(0, (rows - 9 + 1) * (cols - 10 + 1))