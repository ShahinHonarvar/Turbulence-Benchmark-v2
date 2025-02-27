import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.sum(matrix.reshape(-1, 147).T == list(range(147))[np.newaxis, :])