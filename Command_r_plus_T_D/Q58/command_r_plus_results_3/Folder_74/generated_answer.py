import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 1):
        for col in range(col_count - 1):
            if row + 1 < row_count and col + 1 < col_count and (matrix[row, col] + matrix[row, col + 1] + matrix[row + 1, col] + matrix[row + 1, col + 1] == 48):
                submatrix_count += 1
    return submatrix_count