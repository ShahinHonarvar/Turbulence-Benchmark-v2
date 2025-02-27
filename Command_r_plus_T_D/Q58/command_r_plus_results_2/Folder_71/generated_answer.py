import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 78
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            submatrix = matrix[i:, j:]
            if submatrix.size == target_sum:
                count += 1
                break
    return count