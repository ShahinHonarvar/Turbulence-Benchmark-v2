import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=92):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows), range(cols)):
        for r_size, c_size in product(range(r, rows + 1), range(c, cols + 1)):
            submatrix = matrix[r:r_size, c:c_size]
            if submatrix.size == n:
                count += 1
    return count