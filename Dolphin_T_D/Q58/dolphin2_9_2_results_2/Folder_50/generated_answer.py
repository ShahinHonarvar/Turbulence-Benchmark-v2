import numpy as np

def submatrix_with_n_numbers(matrix):
    r, c = matrix.shape
    counter = 0
    for i in range(r - 2):
        for j in range(c - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 40:
                counter += 1
    return counter