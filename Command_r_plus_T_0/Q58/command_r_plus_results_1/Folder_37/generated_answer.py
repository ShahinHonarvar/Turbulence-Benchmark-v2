import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 63):
        for col in range(col_count - 63):
            submatrix = matrix[row:row + 64, col:col + 64]
            if np.count_nonzero(submatrix) == 64:
                submatrix_count += 1
    return submatrix_count