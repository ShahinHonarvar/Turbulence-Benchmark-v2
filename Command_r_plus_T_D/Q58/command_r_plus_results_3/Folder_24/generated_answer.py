import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row_count, col_count = matrix.shape
    target_sum = 51
    count = 0
    for row in range(row_count):
        for col in range(col_count):
            if row_count - row >= 5 and col_count - col >= 5:
                submatrix = matrix[row:row + 5, col:col + 5]
                if submatrix.size == target_sum:
                    count += 1
    return count