import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 138
    for row in range(rows):
        for col in range(cols):
            current_sum = 0
            for r in range(row, rows):
                current_sum += sum(matrix[r, col:])
                if current_sum == target_sum:
                    count += 1
                elif current_sum > target_sum:
                    break
    return count