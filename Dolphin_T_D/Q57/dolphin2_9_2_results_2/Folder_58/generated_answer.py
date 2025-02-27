import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    submatrices = []
    for i1 in range(M):
        for j1 in range(N):
            for i2 in range(i1, M):
                for j2 in range(j1, N):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix)
    return submatrices