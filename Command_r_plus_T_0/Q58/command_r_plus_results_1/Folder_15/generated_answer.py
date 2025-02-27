import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count - 1):
            if matrix[i, j] == matrix[i, j + 1]:
                submatrix_count += 1
    return submatrix_count