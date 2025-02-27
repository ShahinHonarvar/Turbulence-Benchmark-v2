import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = [matrix[i:j, k:l] for i in range(matrix.shape[0]) for j in range(i + 1, matrix.shape[0] + 1) for k in range(matrix.shape[1]) for l in range(k + 1, matrix.shape[1] + 1) if np.sum(matrix[i:j, k:l]) == 80]
    return submatrices