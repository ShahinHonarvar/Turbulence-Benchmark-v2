import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 42
    submatrix_count = 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            for row_end in range(row_start + 1, row_count + 1):
                for col_end in range(col_start + 1, col_count + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == target_sum and submatrix.size == 42:
                        submatrix_count += 1
    return submatrix_count