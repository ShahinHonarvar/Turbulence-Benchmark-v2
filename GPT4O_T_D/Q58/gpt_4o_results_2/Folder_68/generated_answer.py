import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 74
    count = 0
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix_elements = (r2 - r1 + 1) * (c2 - c1 + 1)
                    if submatrix_elements == submatrix_size:
                        count += 1
    return count