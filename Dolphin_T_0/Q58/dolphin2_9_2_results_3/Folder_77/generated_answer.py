import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 2):
        for j in range(n - 2):
            if np.where(matrix[i:i + 3, j:j + 3] == 179)[0].shape[0] == 9:
                count += 1
    return count