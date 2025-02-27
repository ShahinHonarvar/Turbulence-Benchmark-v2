import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_count = 83
    for row_start in range(rows):
        for col_start in range(cols):
            curr_count = 0
            for row_end in range(row_start, rows):
                curr_count += (col_start - cols + 1) * (row_end - row_start + 1)
                if curr_count >= target_count:
                    for col_end in range(col_start, cols):
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        if np.size(submatrix) == target_count:
                            count += 1
    return count