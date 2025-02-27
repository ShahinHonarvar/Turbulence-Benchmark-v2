import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(rows):
        for c in range(cols):
            for sub_rows in range(1, rows - r + 1):
                for sub_cols in range(1, cols - c + 1):
                    if sub_rows * sub_cols == 104:
                        submatrix_count += 1
    return submatrix_count