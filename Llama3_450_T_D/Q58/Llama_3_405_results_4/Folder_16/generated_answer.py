import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_count = 154
    for row in range(rows):
        for col in range(cols):
            curr_count = 0
            for r in range(row, rows):
                curr_count += cols - col
                if curr_count >= target_count:
                    for c in range(col, cols):
                        submatrix_count = (r - row + 1) * (c - col + 1)
                        if submatrix_count == target_count:
                            count += 1
    return count