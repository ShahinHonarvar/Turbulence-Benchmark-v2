import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 144
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            remaining_rows = row_count - row
            remaining_cols = col_count - col
            if remaining_rows * remaining_cols >= target_size:
                submatrix_count += 1
    return submatrix_count