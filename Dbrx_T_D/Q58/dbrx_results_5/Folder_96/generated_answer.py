import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for row in range(matrix_shape[0] - 1):
        for col in range(matrix_shape[1] - 1):
            for width in range(1, matrix_shape[0] - row):
                for height in range(1, matrix_shape[1] - col):
                    submatrix = matrix[row:row + width, col:col + height]
                    if submatrix.size == 20 and np.count_nonzero(submatrix) == 20:
                        submatrix_count += 1
    return submatrix_count