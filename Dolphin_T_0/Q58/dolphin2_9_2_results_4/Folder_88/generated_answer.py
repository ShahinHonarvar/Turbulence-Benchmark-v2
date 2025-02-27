import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.array([matrix[i:i + 67, j:j + 67] for i in range(matrix.shape[0] - 66) for j in range(matrix.shape[1] - 66)]) == 67)