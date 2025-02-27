import numpy as np

def submatrix_with_n_numbers(matrix, n=138):
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    if matrix[row_start:row_end, col_start:col_end].size == n and np.all(matrix[row_start:row_end, col_start:col_end] == 138):
                        count += 1
    return count