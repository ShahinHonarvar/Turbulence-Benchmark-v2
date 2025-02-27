import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    n = 103
    count = 0
    rows, cols = matrix.shape
    for row_start, row_end in product(range(rows), range(rows + 1)):
        for col_start, col_end in product(range(cols), range(cols + 1)):
            if row_end - row_start > 0 and col_end - col_start > 0:
                submatrix = matrix[row_start:row_end, col_start:col_end]
                submatrix_size = submatrix.size
                if submatrix_size == n:
                    count += 1
                elif submatrix_size > n:
                    break
    return count