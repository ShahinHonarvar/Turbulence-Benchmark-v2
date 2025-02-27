import numpy as np

def submatrix_with_n_numbers(matrix):
    return sum([1 for i in range(matrix.shape[0] - 3) for j in range(matrix.shape[1] - 3) if np.all(matrix[i:i + 4, j:j + 4] == 48)])