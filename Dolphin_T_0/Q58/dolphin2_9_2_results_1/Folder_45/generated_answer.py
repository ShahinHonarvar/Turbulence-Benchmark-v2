import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.apply_along_axis(lambda row: np.count_nonzero(np.apply_along_axis(lambda col: np.count_nonzero(row - col == 28), -1, row.reshape(-1, 1)), 1), -1, matrix))