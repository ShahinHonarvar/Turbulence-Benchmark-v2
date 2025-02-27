import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    eight_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            submatrix = matrix[row_start:, col_start:]
            if submatrix.size == 8:
                eight_count += 1
            elif submatrix.size > 8:
                break
    return eight_count