import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i1 in range(m):
        for j1 in range(n):
            for i2 in range(i1, m):
                for j2 in range(j1, n):
                    submatrix_sum = np.sum(matrix[i1:i2, j1:j2])
                    if submatrix_sum == 1:
                        submatrices.append(matrix[i1:i2, j1:j2].tolist())
    return submatrices