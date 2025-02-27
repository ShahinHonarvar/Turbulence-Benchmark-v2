import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 95
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            submatrix = matrix[row_start:, col_start:]
            if submatrix.size >= n:
                submatrix = submatrix[:n]
                submatrix_count += 1
                break
    return submatrix_count