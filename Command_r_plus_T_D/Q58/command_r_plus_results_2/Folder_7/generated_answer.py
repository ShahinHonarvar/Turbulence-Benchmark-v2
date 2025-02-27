import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_row_count, target_col_count = (11, 11)
    if row_count < target_row_count or col_count < target_col_count:
        return 0
    submatrix_count = 0
    for i in range(row_count - target_row_count + 1):
        for j in range(col_count - target_col_count + 1):
            submatrix = matrix[i:i + target_row_count, j:j + target_col_count]
            if submatrix.size == 121:
                submatrix_count += 1
    return submatrix_count