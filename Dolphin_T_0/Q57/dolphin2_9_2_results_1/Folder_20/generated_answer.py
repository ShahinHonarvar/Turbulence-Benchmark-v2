import numpy as np

def submatrix_with_particular_sum(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub = matrix[i:k + 1, j:l + 1].sum()
                    if sub == -57:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices