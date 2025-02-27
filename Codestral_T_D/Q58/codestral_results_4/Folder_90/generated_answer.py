import numpy as np
from scipy import ndimage

def submatrix_with_n_numbers(matrix, n=176):
    window_size = np.sqrt(n)
    if window_size != int(window_size):
        return 0
    window_size = int(window_size)
    window = np.ones((window_size, window_size)) * n
    convolution = ndimage.convolve(matrix, window, mode='constant')
    return np.sum(convolution == n * window_size * window_size)