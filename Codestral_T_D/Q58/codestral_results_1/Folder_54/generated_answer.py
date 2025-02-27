import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def submatrix_with_n_numbers(matrix, n=27):
    view = sliding_window_view(matrix, (3, 3))
    return np.count_nonzero((view.sum(axis=(2, 3)) == n).reshape(-1))