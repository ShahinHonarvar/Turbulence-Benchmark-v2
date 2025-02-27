import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(matrix.reshape((-1, 88)) == 88).item()