import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    sub_matrices = []
    for r1 in range(row):
        for r2 in range(r1, row):
            for c1 in range(col):
                for c2 in range(c1, col):
                    sub_matrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(sub_matrix) == -10:
                        sub_matrices.append(sub_matrix.tolist())
    return sub_matrices