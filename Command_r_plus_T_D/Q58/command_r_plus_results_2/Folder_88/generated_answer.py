import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_size = 67
    submatrix_count = 0
    for row in range(row_count - submatrix_size + 1):
        for col in range(col_count - submatrix_size + 1):
            submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
            if submatrix.size == submatrix_size ** 2:
                submatrix_count += 1
    return submatrix_count