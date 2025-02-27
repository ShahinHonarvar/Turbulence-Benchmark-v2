import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    target_count = 131
    count = 0
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if (bottom - top + 1) * (right - left + 1) == target_count:
                        count += 1
    return count