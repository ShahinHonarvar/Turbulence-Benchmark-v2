import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r + 1, rows + 1):
                for c_end in range(c + 1, cols + 1):
                    submatrix = matrix[r:r_end, c:c_end]
                    if submatrix.size == 67:
                        count += 1
    return count