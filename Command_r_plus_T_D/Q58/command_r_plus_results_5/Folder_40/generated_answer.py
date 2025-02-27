import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise ValueError('Input matrix must contain integers.')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
    return count