import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 131
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == 131 * n:
                count += 1
    return count