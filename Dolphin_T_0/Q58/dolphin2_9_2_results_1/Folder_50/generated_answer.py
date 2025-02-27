import numpy as np

def submatrix_with_n_numbers(matrix, n=40):
    h, w = matrix.shape
    count = 0
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.all(matrix[i:i + n, j:j + n] == 40):
                count += 1
    return count