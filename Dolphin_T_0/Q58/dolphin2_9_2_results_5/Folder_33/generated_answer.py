import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    if matrix.dtype.kind not in 'siu':
        return 0
    n = matrix.size
    if n % 118 != 0:
        return 0
    m = n // 118
    return int(np.prod(np.array(matrix.shape) - m + 1))