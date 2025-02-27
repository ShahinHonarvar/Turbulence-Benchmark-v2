import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    rows, cols = matrix.shape
    total_submatrices = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for sub_rows in range(1, rows - start_row + 1):
                for sub_cols in range(1, cols - start_col + 1):
                    if sub_rows * sub_cols == 15:
                        total_submatrices += 1
    return total_submatrices