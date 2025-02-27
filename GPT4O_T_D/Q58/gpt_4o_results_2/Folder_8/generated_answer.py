import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        return 0
    rows, cols = matrix.shape
    count = 0
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    if (r2 - r1) * (c2 - c1) == 29:
                        count += 1
    return count