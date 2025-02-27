import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy array')
    rows, cols = matrix.shape
    n = 176
    count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_r in range(r, rows):
                for sub_c in range(c, cols):
                    if (sub_r - r + 1) * (sub_c - c + 1) == n:
                        count += 1
    return count