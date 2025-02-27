import numpy as np

def submatrix_with_n_numbers(matrix, n=72):
    if matrix.size == 0:
        return 0
    lengths = np.array(matrix.shape) // n
    if np.any(lengths % 1 != 0):
        return 0
    lengths = np.round(lengths).astype(int)
    return lengths[0] * lengths[1]