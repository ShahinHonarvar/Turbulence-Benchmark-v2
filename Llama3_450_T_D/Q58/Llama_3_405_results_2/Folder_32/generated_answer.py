import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_sum = 103
    for row in range(rows):
        for col in range(cols):
            curr_sum = 0
            for r in range(row, rows):
                curr_sum += np.sum(matrix[r, col:])
                if curr_sum == target_sum:
                    count += 1
                elif curr_sum > target_sum:
                    break
            curr_sum = 0
            for c in range(col, cols):
                curr_sum += np.sum(matrix[row:, c])
                if curr_sum == target_sum:
                    count += 1
                elif curr_sum > target_sum:
                    break
    return count