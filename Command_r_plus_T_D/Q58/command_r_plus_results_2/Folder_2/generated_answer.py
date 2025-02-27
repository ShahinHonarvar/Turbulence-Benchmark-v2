import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 107
    count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            submatrix = matrix[row_start:, col_start:]
            if submatrix.size >= target_sum:
                submatrix = submatrix[:target_sum]
            if submatrix.size == target_sum:
                count += 1
    return count