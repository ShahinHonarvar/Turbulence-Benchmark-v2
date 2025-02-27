import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if matrix[k, l] - matrix[i - 1, l] - matrix[k, j - 1] + matrix[i - 1, j - 1] == 2:
                        submatrices.append(matrix[i - 1:k, j - 1:l])
    if len(submatrices) == 0:
        return []
    else:
        return submatrices