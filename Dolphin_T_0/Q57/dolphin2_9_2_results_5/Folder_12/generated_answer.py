import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    N, M = matrix.shape
    for i in range(N):
        for j in range(M):
            for k in range(i, N):
                for l in range(j, M):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -83:
                        results.append(matrix[i:k + 1, j:l + 1])
    return results