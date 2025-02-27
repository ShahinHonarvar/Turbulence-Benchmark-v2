import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    submatrices = []
    for I in range(M):
        for J in range(N):
            for i in range(I, M):
                for j in range(J, N):
                    if np.sum(matrix[i, j:N]) + np.sum(matrix[i + 1:M, J:i + 1]) == 78:
                        submatrices.append(matrix[I:i + 1, J:j + 1])
    return submatrices