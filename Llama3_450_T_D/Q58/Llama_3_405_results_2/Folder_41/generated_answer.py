import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_count = 73
    for row in range(rows):
        for col in range(cols):
            current_count = 0
            for r in range(row, rows):
                for c in range(col, cols):
                    current_count += 1
                    if current_count == target_count:
                        count += 1
                    elif current_count > target_count:
                        break
                if current_count > target_count:
                    break
    return count