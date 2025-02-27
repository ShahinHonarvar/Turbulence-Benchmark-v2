import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_size = 12
    total_submatrices = 0
    for i in range(row_count - submatrix_size + 1):
        for j in range(col_count - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.count_nonzero(submatrix) == 144:
                total_submatrices += 1
    return total_submatrices