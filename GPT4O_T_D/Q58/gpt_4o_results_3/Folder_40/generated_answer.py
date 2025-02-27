import numpy as np

def submatrix_with_n_numbers(matrix):
    counter_1 = np.count_nonzero(matrix == 1)
    total_count = counter_1 + (matrix.shape[0] - 1) * (matrix.shape[1] - 1)
    return total_count if counter_1 > 0 else 0