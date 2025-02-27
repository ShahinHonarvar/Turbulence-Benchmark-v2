import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    M, N = matrix.shape
    for i in range(M):
        for j in range(N):
            for k in range(i + 1, M):
                for l in range(j + 1, N):
                    submatrix_sum = np.sum(matrix[i:k, j:l])
                    if submatrix_sum == 245:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices