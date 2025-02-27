import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    if n_rows * n_cols < 179:
        return 0
    submatrices_count = 0
    for r1 in range(n_rows):
        for r2 in range(r1, n_rows):
            for c1 in range(n_cols):
                for c2 in range(c1, n_cols):
                    if (r2 - r1 + 1) * (c2 - c1 + 1) == 179:
                        submatrices_count += 1
    return submatrices_count