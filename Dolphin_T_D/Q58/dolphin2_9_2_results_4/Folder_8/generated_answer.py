import numpy as np

def submatrix_with_n_numbers(matrix):
    results = 0
    submatrix_size = 29
    matrix_shape = matrix.shape
    for i in range(0, matrix_shape[0] - submatrix_size + 1):
        for j in range(0, matrix_shape[1] - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            submatrix_count = np.count_nonzero(submatrix)
            if submatrix_count == 29:
                results += 1
    return results