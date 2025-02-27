import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix, n=144):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_size in range(r, rows):
                for c_size in range(c, cols):
                    submatrix = matrix[r:r_size + 1, c:c_size + 1]
                    if submatrix.size == n:
                        count += 1
    return count