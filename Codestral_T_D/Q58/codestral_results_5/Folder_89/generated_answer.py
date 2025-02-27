import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=18):
    rows, cols = matrix.shape
    if rows < np.sqrt(n) or cols < np.sqrt(n):
        return 0
    count = 0
    for r1, c1 in product(range(rows), repeat=2):
        for r2, c2 in product(range(r1, rows), range(c1, cols)):
            if (r2 - r1 + 1) * (c2 - c1 + 1) == n:
                if np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == 18 * n:
                    count += 1
    return count