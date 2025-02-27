import numpy as np

def submatrix_with_n_numbers(matrix):
    return int(np.count_nonzero(matrix.reshape(-1, 185).T.sum(axis=1) == 185))