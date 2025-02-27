import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 95
    matrix_size = np.size(matrix)
    total_submatrices = 0
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            if i + n <= matrix_size[0] and j + n <= matrix_size[1]:
                submatrix = np.array(matrix[i:i + n, j:j + n])
                if np.size(submatrix) == n ** 2:
                    total_submatrices += 1
    return total_submatrices