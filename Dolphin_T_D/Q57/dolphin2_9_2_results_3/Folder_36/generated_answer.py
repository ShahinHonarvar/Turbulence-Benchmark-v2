import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    matrix_sub = matrix[i:k + 1, j:l + 1]
                    if np.sum(matrix_sub) == -779:
                        submatrices.append(matrix_sub)
    return submatrices