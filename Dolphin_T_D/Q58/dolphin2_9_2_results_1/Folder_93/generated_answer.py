import numpy as np
from numpy.lib.stride_tricks import as_strided

def submatrix_with_n_numbers(matrix):
    total = 0
    shape = matrix.shape
    sub_shape = (1, 53)
    matrix = np.asarray(matrix)
    submatrix_count = matrix.shape[0] * matrix.shape[1] - 52
    a_strided = as_strided(matrix, (submatrix_count, 53), (matrix.step[0], 1))
    for n in range(submatrix_count):
        if 53 in np.sum(a_strided, axis=1):
            total += 1
    return total