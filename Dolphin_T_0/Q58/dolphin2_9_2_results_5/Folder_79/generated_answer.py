import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 60
    h, w = matrix.shape
    res = 0
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if (k - i + 1) * (l - j + 1) == n:
                        if np.all(matrix[i:k + 1, j:l + 1] >= 0):
                            res += 1
    return res