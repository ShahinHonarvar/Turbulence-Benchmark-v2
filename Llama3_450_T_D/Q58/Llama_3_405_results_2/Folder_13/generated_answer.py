import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 175
    for row in range(rows):
        for col in range(cols):
            curr_sum = 0
            for sub_row in range(row, rows):
                curr_sum += np.sum(matrix[sub_row, col:])
                if curr_sum == target_sum:
                    count += 1
                elif curr_sum > target_sum:
                    break
            for sub_col in range(col, cols):
                curr_sum = 0
                for sub_row in range(row, rows):
                    curr_sum += matrix[sub_row, sub_col]
                    if curr_sum == target_sum:
                        count += 1
                    elif curr_sum > target_sum:
                        break
    for size in range(2, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                submat = matrix[row:row + size, col:col + size]
                if np.sum(submat) == target_sum:
                    count += 1
    return count