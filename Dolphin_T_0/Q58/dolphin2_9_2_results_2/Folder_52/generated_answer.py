import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy array')
    if len(matrix.shape) != 2:
        raise ValueError('Input must be a 2D matrix')
    n = 147
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            for end_i in range(i + 1, rows + 1):
                for end_j in range(j + 1, cols + 1):
                    submatrix = matrix[i:end_i, j:end_j]
                    if np.count_nonzero(submatrix) == n:
                        counter += 1
    return counter