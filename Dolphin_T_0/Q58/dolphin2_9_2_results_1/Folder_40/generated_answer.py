import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        return 0
    else:
        m, n = matrix.shape
        num_ones = np.where(matrix == 1)
        return len(num_ones[0]) if len(num_ones[0]) == n else 0