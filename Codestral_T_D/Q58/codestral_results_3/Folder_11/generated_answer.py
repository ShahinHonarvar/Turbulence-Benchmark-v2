import numpy as np
from scipy.signal import convolve2d

def submatrix_with_n_numbers(matrix, n=38):
    submatrix_size = 3
    target_sum = n * submatrix_size
    submatrix = np.ones((submatrix_size, submatrix_size))
    convolution_result = convolve2d(matrix, submatrix, mode='valid')
    return np.sum(convolution_result == target_sum)