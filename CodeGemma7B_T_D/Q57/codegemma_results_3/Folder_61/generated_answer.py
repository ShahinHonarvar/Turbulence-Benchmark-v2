import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(m):
                for l in range(k + 1, m + 1):
                    sum = matrix[i][k:l].sum() + matrix[j][k:l].sum()
                    if sum == 8:
                        res.append(matrix[i:j, k:l])
    return res