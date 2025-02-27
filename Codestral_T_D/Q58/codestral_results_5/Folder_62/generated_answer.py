import numpy as np

def submatrix_with_n_numbers(matrix):
    flat_matrix = matrix.flatten()
    window_size = 186
    count = np.sum(np.all(np.lib.stride_tricks.sliding_window_view(flat_matrix, window_size) == 186, axis=1))
    return count