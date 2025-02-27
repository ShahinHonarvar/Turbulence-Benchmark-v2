import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 67
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            remaining_rows = row_count - row_start
            remaining_cols = col_count - col_start
            if remaining_rows * remaining_cols >= target_size:
                submatrix_count += 1
    return submatrix_count