import numpy as np

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    submatrices = []
    for i in range(M):
        for j in range(N):
            for k in range(i, M):
                for l in range(j, N):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 752:
                        submatrices.append(submatrix)
    return submatrices