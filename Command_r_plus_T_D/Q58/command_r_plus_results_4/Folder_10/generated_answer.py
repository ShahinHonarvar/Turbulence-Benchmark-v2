import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_submatrices = 0
    for row in range(row_count):
        for col in range(col_count):
            submatrix = matrix[row:, col:col + 56]
            if submatrix.size == 56:
                total_submatrices += 1
    return total_submatrices