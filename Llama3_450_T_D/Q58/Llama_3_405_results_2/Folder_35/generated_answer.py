import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 111
    for row in range(rows):
        temp = np.zeros(cols)
        for r in range(row, rows):
            temp += matrix[r]
            window_sum = 0
            for c in range(cols):
                window_sum += temp[c]
                if window_sum == target_sum:
                    count += 1
                if window_sum > target_sum:
                    break
                if c > 0:
                    window_sum -= temp[c - 1]
    return count