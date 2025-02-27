import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    row_range = range(shape[0])
    col_range = range(shape[1])
    for i1, i2, j1, j2 in product(row_range, row_range, col_range, col_range):
        if i1 < i2 and j1 < j2 and (i2 - i1 + 1 == j2 - j1 + 1) and ((i2 - i1 + 1) * (j2 - j1 + 1) == 48):
            if np.all(matrix[i1:i2 + 1, j1:j2 + 1] == matrix[i1:i2 + 1, j1:j2 + 1].reshape(6, 8)):
                return 1
    return 0