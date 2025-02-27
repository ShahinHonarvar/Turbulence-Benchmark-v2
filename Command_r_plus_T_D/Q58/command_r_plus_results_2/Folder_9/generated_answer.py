import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 33
    count = 0
    for i in range(row_count - 1):
        for j in range(col_count - 1):
            submatrix_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if submatrix_sum == target_sum:
                count += 1
    return count