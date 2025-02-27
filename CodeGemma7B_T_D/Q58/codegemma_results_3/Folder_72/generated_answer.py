import numpy as np

def submatrix_with_n_numbers(arr):
    rows, cols = arr.shape
    count = 0
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    submatrix = arr[row_start:row_end, col_start:col_end]
                    if np.count_nonzero(submatrix) == 16:
                        count += 1
    return count