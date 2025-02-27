import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    N, M = matrix.shape
    for i in range(N):
        for j in range(M):
            for k in range(i + 1, N):
                for l in range(j + 1, M):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -157:
                        result.append(submatrix)
    return result