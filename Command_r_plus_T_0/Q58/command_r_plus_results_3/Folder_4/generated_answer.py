import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 3):
        for col in range(col_count - 3):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.count_nonzero(submatrix) == 15:
                submatrix_count += 1
    return submatrix_count