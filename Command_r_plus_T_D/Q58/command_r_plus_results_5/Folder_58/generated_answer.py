import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 185
    submatrix_count = 0
    for row in range(row_count + 1 - target_size):
        for col in range(col_count + 1 - target_size):
            submatrix = matrix[row:row + target_size, col:col + target_size]
            if submatrix.size == target_size:
                submatrix_count += 1
    return submatrix_count