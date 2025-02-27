import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 56
    submatrix_count = 0
    for row in range(row_count - 7):
        for col in range(col_count - 7):
            submatrix = matrix[row:row + 8, col:col + 8]
            if submatrix.size == target_size:
                submatrix_count += 1
    return submatrix_count