import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_count = 0
    target_count = 186
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_size == target_count:
                        total_count += 1
    return total_count