import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i, j in np.ndindex(n, m - 1):
        for k, l in zip(np.arange(i, n), np.arange(j, m)):
            if np.sum(matrix[i:k + 1, j:l + 1]) == -44:
                submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices