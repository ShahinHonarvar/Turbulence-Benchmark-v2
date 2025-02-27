import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or (not np.issubdtype(matrix.dtype, np.integer)):
        return 0
    rows, cols = matrix.shape
    if rows * cols < 111:
        return 0
    submatrices_count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    if (row_end - row_start + 1) * (col_end - col_start + 1) == 111:
                        submatrices_count += 1
    return submatrices_count