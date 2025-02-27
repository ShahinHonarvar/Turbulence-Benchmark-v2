import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_count = 74
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            current_count = 0
            for row_end in range(row_start, rows):
                current_count += cols - col_start
                if current_count >= target_count:
                    break
            if current_count < target_count:
                continue
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.size == target_count:
                        count += 1
    return count