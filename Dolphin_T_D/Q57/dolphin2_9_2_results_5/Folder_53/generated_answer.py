import numpy as np

def submatrix_with_particular_sum(mat):
    m, n = mat.shape
    res = []
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    sub = mat[i:k, j:l]
                    if np.sum(sub) == -37:
                        res.append(sub)
    return res