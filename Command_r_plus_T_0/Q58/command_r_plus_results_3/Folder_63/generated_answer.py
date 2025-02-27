import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - 4):
        for j in range(col_count - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 57:
                submatrix_count += 1
    return submatrix_count