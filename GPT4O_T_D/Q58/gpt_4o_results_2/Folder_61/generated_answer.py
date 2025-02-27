import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    if nrows < 2 or ncols < 2:
        return 0
    return (nrows - 1) * (ncols - 1)