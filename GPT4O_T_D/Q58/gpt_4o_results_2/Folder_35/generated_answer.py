import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 111
    if matrix.size < n:
        return 0
    rows, cols = matrix.shape
    total_count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_size == n:
                        total_count += 1
    return total_count