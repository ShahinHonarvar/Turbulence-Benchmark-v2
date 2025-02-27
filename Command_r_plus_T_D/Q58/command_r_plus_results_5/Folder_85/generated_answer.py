import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 13
    submatrix_count = 0
    for row in range(row_count - n + 1):
        for col in range(col_count - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if np.count_nonzero(submatrix) == n:
                submatrix_count += 1
    return submatrix_count