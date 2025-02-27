import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_height, matrix_width = matrix.shape
    for row in range(matrix_height - 2):
        for col in range(matrix_width - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if submatrix.sum() == 193 * 9:
                submatrix_count += 1
    return submatrix_count