import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    target_count = 176
    for row in range(rows):
        for col in range(cols):
            current_count = 0
            for r in range(row, rows):
                current_count += cols - col
                if current_count == target_count:
                    count += 1
                elif current_count > target_count:
                    break
    for col in range(cols):
        for row in range(rows):
            current_count = 0
            for c in range(col, cols):
                current_count += rows - row
                if current_count == target_count:
                    count += 1
                elif current_count > target_count:
                    break
    return count