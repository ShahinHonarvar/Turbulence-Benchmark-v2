import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 138
    if row_count * col_count < target_size:
        return 0
    count = 0
    for row in range(row_count - 1):
        for col in range(col_count - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if submatrix.size == target_size:
                count += 1
    return count