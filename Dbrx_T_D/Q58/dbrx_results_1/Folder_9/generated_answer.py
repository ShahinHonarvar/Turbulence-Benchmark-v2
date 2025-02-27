import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    count = 0
    for i in range(matrix_height - 2):
        for j in range(matrix_width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, 33).all():
                count += 1
    return count