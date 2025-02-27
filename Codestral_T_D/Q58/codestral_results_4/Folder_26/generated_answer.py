import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 115
    h, w = matrix.shape
    count = 0
    for x in range(h):
        for y in range(w):
            for h_sub in range(x, h):
                for w_sub in range(y, w):
                    if np.sum(matrix[x:h_sub + 1, y:w_sub + 1]) == n:
                        count += 1
    return count