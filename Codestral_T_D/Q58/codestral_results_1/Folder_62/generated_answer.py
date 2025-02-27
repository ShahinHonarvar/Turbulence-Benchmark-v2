import numpy as np
from numpy.lib.stride_tricks import as_strided

def submatrix_with_n_numbers(matrix):
    n = int(np.sqrt(matrix.size))
    submatrix_size = int(np.sqrt(186))
    target_sum = 186
    count = 0
    sub_shape = (n - submatrix_size + 1, n - submatrix_size + 1, submatrix_size, submatrix_size)
    view_shape = submatrix_size * submatrix_size
    strides = matrix.strides + matrix.strides
    subs = as_strided(matrix, shape=sub_shape, strides=strides)
    for sub in subs:
        if np.sum(sub) == target_sum:
            count += 1
    return count