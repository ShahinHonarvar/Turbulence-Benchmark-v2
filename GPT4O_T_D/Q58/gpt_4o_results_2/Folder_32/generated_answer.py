import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    nrows, ncols = matrix.shape
    required_count = 103
    for row_start in range(nrows):
        for col_start in range(ncols):
            for row_end in range(row_start, nrows):
                for col_end in range(col_start, ncols):
                    submatrix_size = (row_end - row_start + 1) * (col_end - col_start + 1)
                    if submatrix_size == required_count:
                        total_count += 1
    return total_count