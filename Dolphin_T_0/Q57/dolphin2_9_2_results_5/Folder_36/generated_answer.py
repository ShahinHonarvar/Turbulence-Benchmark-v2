import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i1 in range(n):
        for i2 in range(i1, n):
            for j1 in range(m):
                for j2 in range(j1, m):
                    submatrix_sum = np.sum(matrix[i1:i2 + 1, j1:j2 + 1])
                    if submatrix_sum == -779:
                        submatrices.append(matrix[i1:i2 + 1, j1:j2 + 1])
    return submatrices