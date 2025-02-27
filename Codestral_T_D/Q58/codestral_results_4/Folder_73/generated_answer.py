import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_start, col_start, row_end, col_end in product(range(rows), repeat=4):
        if row_end >= row_start and col_end >= col_start:
            submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
            if np.count_nonzero(submatrix == 41) == submatrix.size:
                count += 1
    return count