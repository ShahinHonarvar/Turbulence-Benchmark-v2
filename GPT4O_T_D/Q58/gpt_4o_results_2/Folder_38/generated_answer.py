import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    total_submatrices = 0
    for rows in range(1, num_rows + 1):
        for cols in range(1, num_cols + 1):
            if rows * cols == 34:
                total_submatrices += (num_rows - rows + 1) * (num_cols - cols + 1)
    return total_submatrices