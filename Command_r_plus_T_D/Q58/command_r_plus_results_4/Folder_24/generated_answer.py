import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_submatrices = 0
    for row in range(row_count - 4):
        for col in range(col_count - 4):
            submatrix = matrix[row:row + 5, col:col + 5]
            if np.count_nonzero(submatrix) == 51:
                total_submatrices += 1
    return total_submatrices