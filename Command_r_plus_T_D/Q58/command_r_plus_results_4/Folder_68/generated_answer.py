import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 74
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            for row_end in range(row_start, row_count):
                for col_end in range(col_start, col_count):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == target_sum and submatrix.size == 74:
                        submatrix_count += 1
    return submatrix_count