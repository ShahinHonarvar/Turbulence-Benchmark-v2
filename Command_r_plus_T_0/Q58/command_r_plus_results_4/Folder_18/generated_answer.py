import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    n = 104
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 10 <= row_count and j + 10 <= col_count:
                submatrix = matrix[i:i + 10, j:j + 10]
                if submatrix.size == n:
                    submatrix_count += 1
    return submatrix_count