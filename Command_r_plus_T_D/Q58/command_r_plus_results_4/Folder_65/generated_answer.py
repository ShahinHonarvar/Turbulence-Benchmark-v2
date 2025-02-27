import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 35
    submatrix_count = 0
    for i in range(row_count):
        for j in range(col_count):
            if i + 4 < row_count and j + 4 < col_count:
                submatrix = matrix[i:i + 5, j:j + 5]
                if np.sum(submatrix) == target_sum:
                    submatrix_count += 1
    return submatrix_count