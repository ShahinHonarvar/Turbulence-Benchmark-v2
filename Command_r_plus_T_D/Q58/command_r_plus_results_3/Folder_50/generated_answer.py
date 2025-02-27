import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 40
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            submatrix_sum = np.sum(matrix[row_start:, col_start:])
            if submatrix_sum == target_sum:
                submatrix_count += 1
    return submatrix_count