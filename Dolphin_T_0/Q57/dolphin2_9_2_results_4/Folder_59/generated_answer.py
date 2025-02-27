import numpy as np

def submatrix_with_particular_sum(mat):
    m, n = mat.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    submat = mat[i:k, j:l]
                    if submat.sum() == 2:
                        submatrices.append(submat)
    return submatrices