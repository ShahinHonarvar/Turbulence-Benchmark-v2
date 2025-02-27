import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 37
    submatrix_count = 0
    for i in range(row_count - 1):
        for j in range(col_count - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.sum(submatrix) == target_sum:
                submatrix_count += 1
    return submatrix_count