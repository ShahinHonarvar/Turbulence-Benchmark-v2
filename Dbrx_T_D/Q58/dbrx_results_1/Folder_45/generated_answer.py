import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_shape = matrix.shape
    height, width = (matrix_shape[0], matrix_shape[1])
    if height < 28 or width < 28:
        return 0
    submatrix_count = 0
    for i in range(height - 27):
        for j in range(width - 27):
            submatrix = matrix[i:i + 28, j:j + 28]
            if np.count_nonzero(submatrix) == 28 * 28:
                submatrix_count += 1
    return submatrix_count