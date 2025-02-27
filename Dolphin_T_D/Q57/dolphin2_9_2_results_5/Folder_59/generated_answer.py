import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    N = len(matrix)
    for i in np.arange(N):
        for j in np.arange(N):
            for i_limit in np.arange(i + 1, N + 1):
                for j_limit in np.arange(j + 1, N + 1):
                    sub = matrix[i:i_limit, j:j_limit]
                    if np.sum(sub) == 2:
                        submatrices.append(sub)
    return submatrices