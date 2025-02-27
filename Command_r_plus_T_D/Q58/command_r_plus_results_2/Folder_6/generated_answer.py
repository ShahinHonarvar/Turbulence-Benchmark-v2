import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 122
    submatrix_count = 0
    for row in range(row_count - target_size + 1):
        for col in range(col_count - target_size + 1):
            submatrix = matrix[row:row + target_size, col:col + target_size]
            if submatrix.size == target_size ** 2:
                submatrix_count += 1
    return submatrix_count