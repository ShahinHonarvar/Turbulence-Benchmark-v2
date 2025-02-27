import numpy as np
import numpy.lib.stride_tricks as np_stride

def submatrix_with_n_numbers(matrix, n=17):
    height, width = matrix.shape
    sub_shape = (height - n + 1, width - n + 1, n, n)
    strides = matrix.strides + matrix.strides
    submatrices = np_stride.as_strided(matrix, shape=sub_shape, strides=strides)
    count = np.sum(np.all(submatrices == 17, axis=(2, 3)))
    return count