import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 1 < row_count and j + 1 < col_count:
                submatrix = matrix[i:i + 2, j:j + 2]
                if submatrix.size == 19:
                    submatrix_count += 1
    return submatrix_count