import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 48
    n_rows, n_cols = matrix.shape
    count = 0
    for i_row in range(n_rows - num_elements + 1):
        for j_col in range(n_cols - num_elements + 1):
            count += (matrix[i_row:i_row + num_elements, j_col:j_col + num_elements] == 48).sum() == num_elements
    return count