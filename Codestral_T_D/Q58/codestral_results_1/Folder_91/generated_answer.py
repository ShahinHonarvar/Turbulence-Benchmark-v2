import numpy as np
from scipy import ndimage

def submatrix_with_n_numbers(matrix, n=5):
    kernel = np.ones((n, n), dtype=int)
    sums = ndimage.convolve(matrix, kernel, mode='constant')
    return np.sum(sums == n * matrix[0, 0])