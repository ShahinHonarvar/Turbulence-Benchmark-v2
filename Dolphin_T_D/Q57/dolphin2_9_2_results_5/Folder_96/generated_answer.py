import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for m in range(i, M):
                for n in range(j, N):
                    submatrix_sum = int(np.sum(matrix[i:m + 1, j:n + 1]))
                    if submatrix_sum == -63:
                        result.append(matrix[i:m + 1, j:n + 1])
    return result