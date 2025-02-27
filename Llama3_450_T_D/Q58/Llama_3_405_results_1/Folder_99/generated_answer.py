import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 146
    for row_start in range(rows):
        for col_start in range(cols):
            current_sum = 0
            for row_end in range(row_start, rows):
                current_sum += np.sum(matrix[row_end, col_start:])
                if current_sum >= target_sum:
                    for col_end in range(col_start, cols):
                        submatrix_sum = np.sum(matrix[row_start:row_end + 1, col_start:col_end + 1])
                        if submatrix_sum == target_sum:
                            count += 1
    return count