import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    total_submatrices = 0
    for row in range(row_count - 1):
        for col in range(col_count - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if submatrix.size == 4 and np.count_nonzero(submatrix) == 4:
                total_submatrices += 1
    return total_submatrices