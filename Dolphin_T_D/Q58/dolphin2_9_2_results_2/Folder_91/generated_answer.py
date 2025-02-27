import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 5
    count = 0
    size = matrix.shape
    for i in range(size[0] - n + 1):
        for j in range(size[1] - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count