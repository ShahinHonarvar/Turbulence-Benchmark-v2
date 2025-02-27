import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 5 < row_count and j + 5 < col_count:
                submatrix = matrix[i:i + 6, j:j + 6]
                if submatrix.size == 64:
                    submatrix_count += 1
    return submatrix_count