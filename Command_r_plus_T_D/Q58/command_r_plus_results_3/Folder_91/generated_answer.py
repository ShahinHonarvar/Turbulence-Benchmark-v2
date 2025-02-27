import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for row in range(row_count - 4):
        for col in range(col_count - 4):
            submatrix = matrix[row:row + 5, col:col + 5]
            if np.count_nonzero(submatrix) == 5:
                submatrix_count += 1
    return submatrix_count