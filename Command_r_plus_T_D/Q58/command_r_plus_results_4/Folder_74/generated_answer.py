import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_submatrix_size = 48
    submatrix_count = 0
    for i in range(row_count - target_submatrix_size + 1):
        for j in range(col_count - target_submatrix_size + 1):
            submatrix = matrix[i:i + target_submatrix_size, j:j + target_submatrix_size]
            if submatrix.size == target_submatrix_size:
                submatrix_count += 1
    return submatrix_count