import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_size = 46
    total_submatrices = 0
    for i in range(row_count - submatrix_size + 1):
        for j in range(col_count - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if submatrix.size == submatrix_size ** 2:
                total_submatrices += 1
    return total_submatrices