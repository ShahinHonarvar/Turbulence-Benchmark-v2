import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 130
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            if row + 3 < row_count and col + 3 < col_count:
                submatrix = matrix[row:row + 3, col:col + 3]
                if submatrix.size == target_sum:
                    submatrix_count += 1
    return submatrix_count