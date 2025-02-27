import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    for r_size in range(1, rows + 1):
        for c_size in range(1, cols + 1):
            if r_size * c_size == 73:
                for r in range(rows - r_size + 1):
                    for c in range(cols - c_size + 1):
                        count += 1
    return count