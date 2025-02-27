import numpy as np

def submatrix_with_particular_sum(mat):
    n = len(mat[0])
    res = []
    for i in range(len(mat)):
        for j in range(n):
            for k in range(i + 1, len(mat)):
                for l in range(j + 1, n):
                    if np.sum(mat[i:k, j:l]) == -50:
                        res.append(mat[i:k, j:l])
    return res