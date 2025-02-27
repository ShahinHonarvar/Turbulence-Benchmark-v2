import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=60):
    rows, cols = matrix.shape
    count = 0
    for r_start, c_start in product(range(rows), range(cols)):
        for r_end, c_end in product(range(r_start, rows), range(c_start, cols)):
            submatrix = matrix[r_start:r_end + 1, c_start:c_end + 1]
            if submatrix.size == n:
                count += 1
    return count