import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for r in range(i, M):
                for c in range(j, N):
                    temp = matrix[i:r + 1, j:c + 1]
                    if np.sum(temp) == -81:
                        result.append(temp)
    return result