import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    max_row = matrix_shape[0] - 1
    max_col = matrix_shape[1] - 1
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            current_submatrix = matrix[row:, col:]
            current_submatrix_shape = current_submatrix.shape
            if current_submatrix_shape[0] >= 3 and current_submatrix_shape[1] >= 3:
                submatrix_elements = np.sum(current_submatrix == 138)
                if submatrix_elements == 9:
                    count += 1
    return count