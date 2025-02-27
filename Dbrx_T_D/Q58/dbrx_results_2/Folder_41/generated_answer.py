import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    possible_rows = matrix_shape[0] - 1
    possible_cols = matrix_shape[1] - 1
    for i in range(possible_rows):
        for j in range(possible_cols):
            current_submatrix = matrix[i:i + 2, j:j + 2]
            if 73 in current_submatrix:
                submatrix_count += 1
    return submatrix_count