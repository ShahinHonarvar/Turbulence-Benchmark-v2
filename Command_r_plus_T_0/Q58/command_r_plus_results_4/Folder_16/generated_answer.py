import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 154
    count = 0
    for row in range(row_count):
        for col in range(col_count):
            submatrix = matrix[row:, col:col + target_sum]
            if submatrix.size == target_sum:
                count += 1
    return count