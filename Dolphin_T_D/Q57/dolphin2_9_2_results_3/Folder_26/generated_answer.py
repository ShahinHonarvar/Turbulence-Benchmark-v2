import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    len_rows, len_cols = matrix.shape
    for r1 in range(len_rows):
        for r2 in range(r1, len_rows):
            for c1 in range(len_cols):
                for c2 in range(c1, len_cols):
                    if np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == 997:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
    return submatrices