import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for rows in range(matrix_shape[0] - 1):
        for cols in range(matrix_shape[1] - 1):
            submatrix = matrix[rows:rows + 2, cols:cols + 2]
            if np.sum(submatrix == 139) == 4:
                count += 1
    return count