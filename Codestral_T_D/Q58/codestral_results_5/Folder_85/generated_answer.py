import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def submatrix_with_n_numbers(matrix, n=13):
    height, width = matrix.shape
    sub_height, sub_width = (height - n + 1, width - n + 1)
    if sub_height < 1 or sub_width < 1:
        return 0
    submatrices = sliding_window_view(matrix, (sub_height, sub_width))
    count = np.sum(np.all(submatrices == 13, axis=(2, 3)))
    return count