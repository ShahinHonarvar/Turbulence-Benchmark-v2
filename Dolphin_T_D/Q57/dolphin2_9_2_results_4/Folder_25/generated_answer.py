import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    if max(matrix[i:k + 1, j:l + 1].sum(), 0) == -20:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices