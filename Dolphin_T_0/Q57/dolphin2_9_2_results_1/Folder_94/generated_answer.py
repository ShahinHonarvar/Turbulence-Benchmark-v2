import numpy as np

def submatrix_with_particular_sum(mat):
    sums = {}
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if i == 0 and j == 0:
                sums[i, j] = mat[i][j]
            elif i == 0:
                sums[i, j] = sums[i, j - 1] + mat[i][j]
            elif j == 0:
                sums[i, j] = sums[i - 1, j] + mat[i][j]
            else:
                sums[i, j] = sums[i - 1, j] + sums[i, j - 1] - sums[i - 1, j - 1] + mat[i][j]
    res = []
    for i1 in range(mat.shape[0]):
        for j1 in range(mat.shape[1]):
            for i2 in range(i1, mat.shape[0]):
                for j2 in range(j1, mat.shape[1]):
                    if sums[i2, j2] - sums[i2, j1 - 1] - sums[i1 - 1, j2] + sums[i1 - 1, j1 - 1] == 92:
                        res.append(mat[i1:i2 + 1, j1:j2 + 1])
    return res