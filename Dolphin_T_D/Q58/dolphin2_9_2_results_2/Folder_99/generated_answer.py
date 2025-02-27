import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    submatrices = 0
    num_submatrix = 146
    index = np.arange(matrix.size)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + num_submatrix <= matrix.shape[0] and j + num_submatrix <= matrix.shape[1]:
                sub_matrix = matrix[i:i + num_submatrix, j:j + num_submatrix]
                if sub_matrix.size == num_submatrix:
                    submatrices += 1
    return submatrices