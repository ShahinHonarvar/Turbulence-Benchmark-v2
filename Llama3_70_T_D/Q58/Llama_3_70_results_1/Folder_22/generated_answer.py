import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_size in range(1, rows - r + 1):
                for c_size in range(1, cols - c + 1):
                    if r_size * c_size == 21:
                        count += 1
    return count