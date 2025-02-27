import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = np.shape(matrix)
    count = 0
    for row_count in range(1, rows + 1):
        for col_count in range(1, cols + 1):
            for row_start in range(rows - row_count + 1):
                for col_start in range(cols - col_count + 1):
                    if row_count * col_count == 57:
                        count += 1
    return count