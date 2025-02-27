import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=53):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows), range(cols)):
        for rr, cc in product(range(r, rows + 1), range(c, cols + 1)):
            if (rr - r) * (cc - c) == n:
                count += 1
    return count