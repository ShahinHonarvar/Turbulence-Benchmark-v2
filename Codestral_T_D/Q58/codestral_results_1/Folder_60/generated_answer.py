import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = int(np.sqrt(88))
    matrix_size = matrix.shape
    count = 0
    for i in range(matrix_size[0] - submatrix_size + 1):
        for j in range(matrix_size[1] - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == 88:
                count += 1
    return count