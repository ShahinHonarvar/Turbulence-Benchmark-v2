import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=56):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows), range(cols)):
        for r_end, c_end in product(range(r, rows), range(c, cols)):
            if (r_end - r + 1) * (c_end - c + 1) == n:
                count += 1
    return count