import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    possible_row_counts = range(1, matrix_shape[0] - 1)
    possible_col_counts = range(1, matrix_shape[1] - 1)
    for row_count in possible_row_counts:
        for col_count in possible_col_counts:
            submatrix = matrix[:row_count, :col_count]
            if submatrix.size == 67 and 67 in submatrix:
                count += 1
    return count