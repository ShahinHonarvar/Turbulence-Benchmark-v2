import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - 3):
        for j in range(col_count - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 16:
                submatrix_count += 1
    return submatrix_count