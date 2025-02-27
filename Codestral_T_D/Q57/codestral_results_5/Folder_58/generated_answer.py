import numpy as np

def submatrix_with_particular_sum(matrix):
    r, c = matrix.shape
    res = []
    for i in range(r):
        for j in range(c):
            for k in range(i + 1, r + 1):
                for l in range(j + 1, c + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -137:
                        res.append(submatrix)
    return res