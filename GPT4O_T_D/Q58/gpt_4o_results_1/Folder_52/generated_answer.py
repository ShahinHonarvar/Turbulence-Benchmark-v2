import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    num_elements = 147
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(1, rows - i + 1):
                for sub_cols in range(1, cols - j + 1):
                    if sub_rows * sub_cols == num_elements:
                        total_count += 1
    return total_count