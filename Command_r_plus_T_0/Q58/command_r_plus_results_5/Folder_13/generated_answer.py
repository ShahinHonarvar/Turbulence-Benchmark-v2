import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_size = 175
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            if (row + 1) * (col + 1) == target_size:
                submatrix_count += 1
            elif (row + 1) * (col + 1) > target_size:
                break
    return submatrix_count