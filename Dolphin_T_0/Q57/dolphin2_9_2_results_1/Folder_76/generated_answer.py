import numpy as np

def submatrix_with_particular_sum(matrix):
    row_len, col_len = matrix.shape
    sub_matrices = []
    for r1 in range(row_len):
        for r2 in range(r1 + 1, row_len):
            for c1 in range(col_len):
                for c2 in range(c1 + 1, col_len):
                    submatrix_sum = np.sum(matrix[r1:r2, c1:c2])
                    if submatrix_sum == -255:
                        sub_matrices.append(matrix[r1:r2, c1:c2])
    return sub_matrices