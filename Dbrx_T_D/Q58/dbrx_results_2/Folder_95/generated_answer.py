import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    max_row, max_col = (matrix_shape[0] - 1, matrix_shape[1] - 1)
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            current_submatrix = matrix[row:row + 2, col:col + 2]
            if 87 in np.unique(current_submatrix):
                count += 1
    return count