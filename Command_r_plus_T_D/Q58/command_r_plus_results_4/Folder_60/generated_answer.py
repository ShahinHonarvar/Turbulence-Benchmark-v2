import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - 7):
        for j in range(col_count - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.count_nonzero(submatrix) == 88:
                submatrix_count += 1
    return submatrix_count