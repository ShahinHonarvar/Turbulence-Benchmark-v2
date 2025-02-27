import numpy as np

def submatrix_with_particular_sum(mat):
    n, m = mat.shape
    res = []
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    if np.sum(mat[i:k, j:l]) == -93:
                        res.append(mat[i:k, j:l])
    return res