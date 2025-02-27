import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 90
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if (i + 2) * (j + 2) >= n:
                submatrix_count += 1
                break
    return submatrix_count