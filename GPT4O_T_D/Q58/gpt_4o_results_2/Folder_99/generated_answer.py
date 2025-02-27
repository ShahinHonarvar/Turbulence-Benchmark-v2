import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    required_elements = 146
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    submatrix_size = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_size == required_elements:
                        count += 1
    return count