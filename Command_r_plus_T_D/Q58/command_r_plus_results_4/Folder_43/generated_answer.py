import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 85
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 7 < row_count and j + 7 < col_count:
                submatrix = matrix[i:i + 8, j:j + 8]
                if submatrix.size == n:
                    submatrix_count += 1
    return submatrix_count