import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_sum = 104
    for r in range(rows):
        for c in range(cols):
            curr_sum = 0
            for i in range(r, rows):
                curr_sum += np.sum(matrix[i, c:])
                if curr_sum == target_sum:
                    count += 1
                if curr_sum > target_sum:
                    break
    return count