import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 104
    count = 0
    for row in range(row_count - 1):
        for col in range(col_count - 1):
            submatrix_sum = matrix[row, col] + matrix[row, col + 1] + matrix[row + 1, col] + matrix[row + 1, col + 1]
            if submatrix_sum == target_sum:
                count += 1
    return count