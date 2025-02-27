import numpy as np

def submatrix_with_n_numbers(matrix):
    num_elements = 120
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for n_row in range(i, n_rows):
                for n_col in range(j, n_cols):
                    if (n_row + 1 - i) * (n_col + 1 - j) == num_elements:
                        count += 1
    return count