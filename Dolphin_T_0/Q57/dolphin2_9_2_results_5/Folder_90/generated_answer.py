import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for k in range(i + 1, M + 1):
                for l in range(j + 1, N + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -452:
                        submatrices.append(submatrix)
    return submatrices