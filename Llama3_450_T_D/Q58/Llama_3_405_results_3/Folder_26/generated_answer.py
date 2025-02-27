import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_sum = 115
    rows, cols = matrix.shape
    prefix_sum = np.zeros((rows + 1, cols + 1))
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum[i, j] = matrix[i - 1, j - 1] + prefix_sum[i - 1, j] + prefix_sum[i, j - 1] - prefix_sum[i - 1, j - 1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for end_col in range(j, cols):
                    curr_sum = prefix_sum[k + 1, end_col + 1] - prefix_sum[k + 1, j] - prefix_sum[i, end_col + 1] + prefix_sum[i, j]
                    if curr_sum == target_sum:
                        count += 1
    return count