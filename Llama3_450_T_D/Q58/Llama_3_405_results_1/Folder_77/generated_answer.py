import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 179
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            current_sum = 0
            for row_end in range(row_start, rows):
                current_sum += np.sum(matrix[row_end, col_start:col_start + target_count])
                if current_sum == target_count:
                    count += 1
                    break
                elif current_sum > target_count:
                    break
    for col_start in range(cols):
        for row_start in range(rows):
            current_sum = 0
            for col_end in range(col_start, cols):
                current_sum += np.sum(matrix[row_start:row_start + target_count, col_end])
                if current_sum == target_count:
                    count += 1
                    break
                elif current_sum > target_count:
                    break
    for size in range(2, min(rows, cols) + 1):
        for row_start in range(rows - size + 1):
            for col_start in range(cols - size + 1):
                submatrix_sum = np.sum(matrix[row_start:row_start + size, col_start:col_start + size])
                if submatrix_sum == target_count:
                    count += 1
    return count