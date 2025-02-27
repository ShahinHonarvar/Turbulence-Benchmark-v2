import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    n_rows, n_cols = matrix.shape
    for r1 in range(n_rows):
        for r2 in range(r1, n_rows):
            for c1 in range(n_cols):
                for c2 in range(c1, n_cols):
                    if matrix[r1:r2 + 1, c1:c2 + 1].sum() == -20:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result