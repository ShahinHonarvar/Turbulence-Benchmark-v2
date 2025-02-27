import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 104
    for row in range(rows):
        for col in range(cols):
            current_sum = 0
            for sub_row in range(row, rows):
                current_sum += np.sum(matrix[sub_row, col:])
                if current_sum == target_sum:
                    count += 1
                elif current_sum > target_sum:
                    break
                for sub_col in range(col + 1, cols):
                    current_sum -= np.sum(matrix[row:sub_row + 1, col:sub_col])
                    if current_sum == target_sum:
                        count += 1
                    elif current_sum < target_sum:
                        break
    return count