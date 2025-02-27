import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=193):
    rows, cols = matrix.shape
    total = 0
    for row_start, col_start in product(range(rows), range(cols)):
        for row_end, col_end in product(range(row_start, rows), range(col_start, cols)):
            submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
            if submatrix.size == n:
                total += 1
    return total