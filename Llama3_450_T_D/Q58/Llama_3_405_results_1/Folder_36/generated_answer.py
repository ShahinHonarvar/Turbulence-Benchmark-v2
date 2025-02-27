import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 131
    for row in range(rows):
        for col in range(cols):
            curr_sum = 0
            for r in range(row, rows):
                curr_sum += np.sum(matrix[r, col:col + n])
                if curr_sum == n and (r - row + 1) * n == n:
                    count += 1
                if curr_sum > n:
                    break
    return count