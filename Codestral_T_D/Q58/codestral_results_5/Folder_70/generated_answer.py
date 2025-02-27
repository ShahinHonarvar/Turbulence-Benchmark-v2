import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 173
    h, w = matrix.shape
    count = 0
    for x in range(h):
        for y in range(w):
            for i in range(x, h):
                for j in range(y, w):
                    if np.sum(matrix[x:i + 1, y:j + 1]) == n * ((i - x + 1) * (j - y + 1)):
                        count += 1
    return count