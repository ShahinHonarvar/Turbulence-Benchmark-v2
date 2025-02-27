import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 131
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 13 <= row_count and j + 13 <= col_count:
                submatrix = matrix[i:i + 13, j:j + 13]
                if submatrix.size == n:
                    submatrix_count += 1
    return submatrix_count