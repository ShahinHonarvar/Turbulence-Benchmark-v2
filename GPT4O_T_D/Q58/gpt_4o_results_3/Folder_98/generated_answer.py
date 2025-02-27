import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy array')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional array')
    rows, cols = matrix.shape
    if rows < 3 or cols < 3:
        return 0
    count = (rows - 2) * (cols - 2)
    return count