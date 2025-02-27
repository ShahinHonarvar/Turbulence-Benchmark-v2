import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i1 in range(m):
        for j1 in range(n):
            for i2 in range(i1 + 1, m + 1):
                for j2 in range(j1 + 1, n + 1):
                    sub_matrix = matrix[i1:i2, j1:j2]
                    if np.sum(sub_matrix) == 3:
                        submatrices.append(sub_matrix)
    return submatrices