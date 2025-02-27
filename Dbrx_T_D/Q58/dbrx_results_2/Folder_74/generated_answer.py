import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    submatrix_size = 48
    count = 0
    for i in range(matrix_height - submatrix_size + 1):
        for j in range(matrix_width - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.all(submatrix == 48):
                count += 1
    return count