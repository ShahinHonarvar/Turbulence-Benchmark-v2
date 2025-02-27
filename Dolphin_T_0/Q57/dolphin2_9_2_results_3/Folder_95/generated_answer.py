import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for k in range(n):
        for i in range(k, n + 1):
            for j in range(m):
                submatrix_sum = matrix[k:i, j:j + 1].sum()
                if submatrix_sum == 19:
                    submatrices.append(matrix[k:i, j:j + 1].tolist())
    for k in range(m):
        for i in range(k, m + 1):
            for j in range(n):
                submatrix_sum = matrix[j:j + 1, k:i].sum()
                if submatrix_sum == 19:
                    submatrices.append(matrix[j:j + 1, k:i].tolist())
    return submatrices