import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix_sum = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    submatrix_dimensions = np.tril_indices(matrix_sum.shape[0], matrix_sum.shape[1], k=-1)
    result = []
    for r0 in submatrix_dimensions[0]:
        for c0 in submatrix_dimensions[1]:
            for r1 in range(r0, matrix_sum.shape[0]):
                for c1 in range(c0, matrix_sum.shape[1]):
                    submatrix_sum = matrix_sum[r1][c1] - matrix_sum[r0][c1] - matrix_sum[r1][c0] + matrix_sum[r0][c0]
                    if submatrix_sum == 0:
                        result.append((r0, c0, r1, c1))
    return result