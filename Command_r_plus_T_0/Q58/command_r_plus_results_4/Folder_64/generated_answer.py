import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 6):
        for col in range(col_count - 6):
            submatrix = matrix[row:row + 7, col:col + 7]
            if np.count_nonzero(submatrix) == 7:
                submatrix_count += 1
    return submatrix_count