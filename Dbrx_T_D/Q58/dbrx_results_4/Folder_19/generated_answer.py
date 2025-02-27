import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    submatrix_count = 0
    submatrix_height = 3
    submatrix_width = 3
    for i in range(matrix_height - submatrix_height + 1):
        for j in range(matrix_width - submatrix_width + 1):
            submatrix = matrix[i:i + submatrix_height, j:j + submatrix_width]
            if np.sum(submatrix) == 17 * submatrix_height * submatrix_width:
                submatrix_count += 1
    return submatrix_count