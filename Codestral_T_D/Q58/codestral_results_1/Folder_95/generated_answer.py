import numpy as np
from scipy.signal import convolve2d

def submatrix_with_n_numbers(matrix, n=87):
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0
    counts = convolve2d(matrix == n, kernel, mode='valid')
    return np.sum(counts == 9)