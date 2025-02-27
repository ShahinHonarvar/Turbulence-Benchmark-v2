import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 54
    count = 0
    m, n = matrix.shape
    for i in range(m - n + 1):
        for j in range(n - n + 1):
            if np.all(matrix[i:i + n, j:j + n] == 54):
                count += 1
    return count