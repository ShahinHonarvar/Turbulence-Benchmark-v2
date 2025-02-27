import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 146
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 14 <= row_count and j + 14 <= col_count:
                submatrix_count += 1
    return submatrix_count