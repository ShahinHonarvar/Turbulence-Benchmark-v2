import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i0 in range(m):
        for i1 in range(i0, m):
            for j0 in range(n):
                for j1 in range(j0, n):
                    submatrix = matrix[i0:i1 + 1, j0:j1 + 1]
                    if np.sum(submatrix) == 901:
                        submatrices.append(submatrix)
    return submatrices