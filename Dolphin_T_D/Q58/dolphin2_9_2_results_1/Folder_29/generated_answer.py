import numpy as np
from scipy.signal import convolve2d

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    n_size = 19
    submatrix_count = 0
    for i in range(m - n_size + 1):
        for j in range(n - n_size + 1):
            if convolve2d(matrix[i:i + n_size, j:j + n_size], np.ones((n_size, n_size)), 'same', 'valid').sum() == n_size:
                submatrix_count += 1
    return submatrix_count