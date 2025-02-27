import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 68):
        for col in range(col_count - 68):
            submatrix = matrix[row:row + 69, col:col + 69]
            if np.count_nonzero(submatrix) == 69:
                submatrix_count += 1
    return submatrix_count