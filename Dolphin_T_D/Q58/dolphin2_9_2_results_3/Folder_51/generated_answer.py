import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape
    for i in range(matrix_size[0] - 2):
        for j in range(matrix_size[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == 95:
                count += 1
    return count