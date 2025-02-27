import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m + 1):
        for j in range(n + 1):
            for p in range(i, m):
                for q in range(j, n):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if submatrix.sum() == 382:
                        submatrices.append(submatrix)
    return submatrices