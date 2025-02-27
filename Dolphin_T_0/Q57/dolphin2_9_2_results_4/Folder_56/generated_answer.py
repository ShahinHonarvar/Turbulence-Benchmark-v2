import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for s in range(1, min(M - i + 1, N - j + 1)):
                submatrix = matrix[i:i + s, j:j + s]
                if np.sum(submatrix) == -50:
                    submatrices.append(submatrix)
    return submatrices