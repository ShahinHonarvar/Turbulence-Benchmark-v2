import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    num_elements = (row_end - row_start + 1) * (col_end - col_start + 1)
                    if num_elements == 69:
                        count += 1
    return count