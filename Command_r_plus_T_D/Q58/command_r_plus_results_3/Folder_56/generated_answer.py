import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 2 <= row_count and j + 2 <= col_count:
                submatrix = matrix[i:i + 3, j:j + 3]
                if submatrix.size == 68:
                    submatrix_count += 1
    return submatrix_count