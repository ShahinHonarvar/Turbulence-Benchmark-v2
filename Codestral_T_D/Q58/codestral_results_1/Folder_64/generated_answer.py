import numpy as np

def submatrix_with_n_numbers(matrix, n=7):
    if matrix.size < n:
        return 0
    submatrix_size = int(np.sqrt(n))
    if submatrix_size * submatrix_size != n:
        raise ValueError('n must be a perfect square')
    window_shape = (matrix.shape[0] - submatrix_size + 1, matrix.shape[1] - submatrix_size + 1, submatrix_size, submatrix_size)
    strides = matrix.strides + matrix.strides
    submatrices = np.lib.stride_tricks.as_strided(matrix, shape=window_shape, strides=strides)
    return np.sum(submatrices.reshape(submatrices.shape[0] * submatrices.shape[1], -1).sum(axis=1) == 7)