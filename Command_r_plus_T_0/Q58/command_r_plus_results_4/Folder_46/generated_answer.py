import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 144
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            if row + 3 < row_count and col + 3 < col_count:
                submatrix = matrix[row:row + 4, col:col + 4]
                if submatrix.size == target_size:
                    submatrix_count += 1
    return submatrix_count