import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_submatrices = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    num_elements = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if num_elements == 41:
                        total_submatrices += 1
                    elif num_elements > 41:
                        break
    return total_submatrices