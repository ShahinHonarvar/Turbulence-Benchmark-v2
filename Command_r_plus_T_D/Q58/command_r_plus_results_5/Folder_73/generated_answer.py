import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 41
    submatrix_count = 0
    for i in range(row_count - n + 1):
        for j in range(col_count - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix) == n:
                submatrix_count += 1
    return submatrix_count