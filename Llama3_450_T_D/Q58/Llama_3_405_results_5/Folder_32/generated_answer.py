import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 103
    for row in range(rows):
        temp = np.zeros(cols)
        for r in range(row, rows):
            temp += matrix[r]
            window_sum = 0
            start = 0
            for end in range(cols):
                window_sum += temp[end]
                while start <= end and window_sum > target_sum:
                    window_sum -= temp[start]
                    start += 1
                if window_sum == target_sum:
                    count += 1
    return count