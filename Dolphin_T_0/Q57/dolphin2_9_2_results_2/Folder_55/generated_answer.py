import numpy as np

def submatrix_with_particular_sum(matrix):
    N = len(matrix)
    submatrices = []
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 1:
                        submatrices.append(submatrix.tolist())
    return submatrices