import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for i in range(h - 2):
        for j in range(w - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 185:
                count += 1
    return count