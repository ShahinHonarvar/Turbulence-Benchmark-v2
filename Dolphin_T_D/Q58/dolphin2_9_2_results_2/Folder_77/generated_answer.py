import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            if (i + 2 < h and j + 2 < w) and np.all(matrix[i:i + 2, j:j + 2] == 179):
                count += 1
    return count