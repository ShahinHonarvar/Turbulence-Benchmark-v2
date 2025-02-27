import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    n = 74
    count = 0
    for y in range(h):
        for x in range(w):
            for hh in range(y, h):
                for ww in range(x, w):
                    if np.sum(matrix[y:hh + 1, x:ww + 1]) == n * (matrix[y, x] if y == hh and x == ww else 1):
                        count += 1
    return count