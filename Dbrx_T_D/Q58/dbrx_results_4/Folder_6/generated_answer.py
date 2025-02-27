import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input matrix must be a two-dimensional numpy matrix of integers.')
    height, width = matrix.shape
    count = 0
    for i in range(height - 1):
        for j in range(width - 1):
            if np.count_nonzero(matrix[i:i + 2, j:j + 2] == 122) == 4:
                count += 1
    return count