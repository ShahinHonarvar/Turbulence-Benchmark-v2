import numpy as np

def submatrix_with_n_numbers(matrix):
    sub_matrix_count = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 4):
            sub_matrix = matrix[i:i + 5, j:j + 5]
            if np.all(sub_matrix == 95):
                sub_matrix_count += 1
    return sub_matrix_count