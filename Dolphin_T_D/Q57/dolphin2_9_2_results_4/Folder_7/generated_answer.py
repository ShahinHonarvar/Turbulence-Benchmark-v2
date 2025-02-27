import numpy as np

def submatrix_with_particular_sum(mat):
    submatrices = []
    m, n = mat.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix_sum = np.sum(mat[i:k + 1, j:l + 1])
                    if submatrix_sum == -128:
                        submatrices.append(mat[i:k + 1, j:l + 1])
    return submatrices