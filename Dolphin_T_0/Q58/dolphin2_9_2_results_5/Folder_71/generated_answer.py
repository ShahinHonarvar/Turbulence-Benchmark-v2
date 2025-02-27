import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    h, w = matrix.shape
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if (k - i + 1) * (l - j + 1) == 78:
                        result += 1
    return result