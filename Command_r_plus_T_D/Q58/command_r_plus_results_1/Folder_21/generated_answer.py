import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    rows, cols = matrix.shape
    target_sum = 139
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            if submatrix_sum == target_sum:
                count += 1
    return count