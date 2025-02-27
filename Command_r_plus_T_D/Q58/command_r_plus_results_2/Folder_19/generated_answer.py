import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 17
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            if row_start + 2 <= row_count and col_start + 2 <= col_count:
                submatrix = matrix[row_start:row_start + 2, col_start:col_start + 2]
                if submatrix.size == target_sum:
                    submatrix_count += 1
    return submatrix_count