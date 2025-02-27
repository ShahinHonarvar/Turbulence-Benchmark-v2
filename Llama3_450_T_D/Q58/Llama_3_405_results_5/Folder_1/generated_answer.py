import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_count = 23
    for row_start in range(rows):
        for col_start in range(cols):
            numbers_count = 0
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    numbers_count += 1
                    if numbers_count == target_count:
                        count += 1
                    if numbers_count > target_count:
                        break
                if numbers_count > target_count:
                    break
    return count