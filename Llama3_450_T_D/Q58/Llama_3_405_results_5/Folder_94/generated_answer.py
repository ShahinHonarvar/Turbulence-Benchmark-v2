import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_sum = 93
    for row in range(rows):
        temp = [0] * cols
        for r in range(row, rows):
            for col in range(cols):
                temp[col] += matrix[r, col]
            for c in range(cols):
                curr_sum = 0
                for j in range(c, cols):
                    curr_sum += temp[j]
                    if curr_sum == target_sum:
                        count += 1
    return count