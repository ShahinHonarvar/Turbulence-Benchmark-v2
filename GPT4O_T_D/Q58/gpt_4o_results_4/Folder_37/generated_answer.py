import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    submatrix_size = 64
    found_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(1, rows - i + 1):
                for sub_cols in range(1, cols - j + 1):
                    if sub_rows * sub_cols == submatrix_size:
                        found_submatrices += 1
    return found_submatrices