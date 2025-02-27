import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape
    for i_row in range(rows):
        for j_col in range(cols):
            if np.sum(matrix[i_row:i_row + 7, j_col:j_col + 7]) == 49:
                submatrix_count += 1
    if submatrix_count == 0:
        return 0
    else:
        return submatrix_count