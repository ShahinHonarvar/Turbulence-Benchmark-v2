import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    M = len(matrix[0])
    submatrices = []
    for i in range(N):
        for j in range(M):
            for k in range(i + 1, N + 1):
                for l in range(j + 1, M + 1):
                    if np.sum(matrix[i:k, j:l]) == 54:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices