import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_height, matrix_width = matrix.shape
    for i in range(matrix_height - 1):
        for j in range(matrix_width - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix == 154) == 4:
                submatrix_count += 1
    return submatrix_count