import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_count = 66
    for row_start in range(rows):
        for col_start in range(cols):
            curr_count = 0
            for row_end in range(row_start, rows):
                curr_count += cols - col_start
                if curr_count >= target_count:
                    count += 1
                curr_count -= row_end - row_start + 1
                if row_end - row_start + 1 > target_count:
                    break
                for col_end in range(col_start + 1, cols):
                    curr_count += row_end - row_start + 1
                    if curr_count == target_count:
                        count += 1
                    elif curr_count > target_count:
                        break
    return count