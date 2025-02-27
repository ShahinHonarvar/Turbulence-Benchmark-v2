import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 95
    for row in range(rows):
        temp_sum = 0
        for col in range(cols):
            temp_sum += matrix[row, col]
            if temp_sum == target_sum:
                count += 1
            elif temp_sum > target_sum:
                break
            for r in range(row + 1, rows):
                temp_sum += matrix[r, col]
                if temp_sum == target_sum:
                    count += 1
                elif temp_sum > target_sum:
                    break
    for col in range(cols):
        temp_sum = 0
        for row in range(rows):
            temp_sum += matrix[row, col]
            if temp_sum == target_sum:
                count += 1
            elif temp_sum > target_sum:
                break
            for c in range(col + 1, cols):
                temp_sum += matrix[row, c]
                if temp_sum == target_sum:
                    count += 1
                elif temp_sum > target_sum:
                    break
    return count