import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input must be a numpy ndarray.')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional matrix.')
    if not np.issubdtype(matrix.dtype, np.integer):
        raise TypeError('Matrix elements must be integers.')
    target_sum = 27
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix_sum = matrix[i, j] + matrix[i, j + 1] + matrix[i + 1, j] + matrix[i + 1, j + 1]
            if submatrix_sum == target_sum:
                count += 1
    return count