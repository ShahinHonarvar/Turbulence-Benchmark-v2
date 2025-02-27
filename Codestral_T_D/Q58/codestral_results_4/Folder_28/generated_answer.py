import numpy as np
from scipy.signal import convolve2d

def submatrix_with_n_numbers(matrix, n=37):
    filter_matrix = np.ones((3, 3)) * n
    result = convolve2d(matrix, filter_matrix, mode='valid')
    return np.sum(result == n * 9)