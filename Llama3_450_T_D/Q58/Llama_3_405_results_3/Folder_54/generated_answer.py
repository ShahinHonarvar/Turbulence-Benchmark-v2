import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    n = 27
    for row in range(rows):
        for col in range(cols):
            curr_count = 0
            rows_left = rows - row
            cols_left = cols - col
            for r in range(rows_left):
                for c in range(cols_left):
                    curr_count += 1
                    if curr_count == n:
                        count += 1
                        curr_count -= 1
    return count