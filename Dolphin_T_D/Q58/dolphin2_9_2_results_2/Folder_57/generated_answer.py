import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.size
    result = 0
    for sub_matrix_size in range(2, size + 1):
        for i in range(size - sub_matrix_size + 1):
            for j in range(size - sub_matrix_size + 1):
                if np.count_nonzero(matrix[i:sub_matrix_size + i, j:sub_matrix_size + j]) == 92:
                    result += 1
    return result