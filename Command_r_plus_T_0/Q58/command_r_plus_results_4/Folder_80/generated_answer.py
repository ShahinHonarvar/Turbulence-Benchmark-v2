import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 180
    submatrix_count = 0
    for row in range(row_count):
        for col in range(col_count):
            submatrix = matrix[row:row + 2, col:col + 2]
            if submatrix.size == 4 and np.sum(submatrix) == target_sum:
                submatrix_count += 1
    return submatrix_count