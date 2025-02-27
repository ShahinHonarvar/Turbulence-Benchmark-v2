import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 73
    for row in range(rows):
        for col in range(cols):
            curr_sum = 0
            for i in range(row, rows):
                curr_sum += np.sum(matrix[i, col:])
                if curr_sum == target_sum:
                    count += 1
                elif curr_sum > target_sum:
                    break
    return count