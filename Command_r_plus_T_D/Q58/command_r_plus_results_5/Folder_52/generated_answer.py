import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    num_rows, num_cols = matrix.shape
    target_sum = 147
    count = 0
    for row in range(num_rows - 1):
        for col in range(num_cols - 1):
            submatrix_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            if submatrix_sum == target_sum:
                count += 1
    return count