import numpy as np

def submatrix_with_particular_sum(matrix):
    M = len(matrix)
    N = len(matrix[0])
    submatrices = []
    for i in range(0, M):
        for j in range(0, N):
            for k in range(i, M):
                for l in range(j, N):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(submatrix) == 77:
                        submatrices.append(submatrix)
    return submatrices