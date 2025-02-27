import numpy as np

def submatrix_with_n_numbers(matrix):
    number_of_submatrices = 0
    matrix_shape = matrix.shape
    max_size = min(matrix_shape)
    for submatrix_size in range(max_size - 1, 0, -1):
        for row in range(matrix_shape[0] - submatrix_size + 1):
            for col in range(matrix_shape[1] - submatrix_size + 1):
                submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
                if np.all(submatrix == submatrix) and np.count_nonzero(submatrix) == 10:
                    number_of_submatrices += 1
    return number_of_submatrices