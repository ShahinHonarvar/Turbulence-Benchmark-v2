import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i0 in range(m):
        for i1 in range(i0, m):
            for j0 in range(n):
                for j1 in range(j0, n):
                    if np.sum(matrix[i0:i1 + 1, j0:j1 + 1]) == 17:
                        submatrices.append(matrix[i0:i1 + 1, j0:j1 + 1])
    return submatrices