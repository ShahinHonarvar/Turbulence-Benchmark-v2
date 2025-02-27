import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 33
    count = 0
    for row in range(row_count - 2):
        for col in range(col_count - 2):
            submatrix_sum = np.sum(matrix[row:row + 3, col:col + 3])
            if submatrix_sum == target_sum:
                count += 1
    return count