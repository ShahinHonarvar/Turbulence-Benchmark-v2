import numpy as np

def submatrix_with_n_numbers(matrix):
    return int(np.count_nonzero(np.apply_along_axis(lambda x: 66 in x, 1, matrix)))