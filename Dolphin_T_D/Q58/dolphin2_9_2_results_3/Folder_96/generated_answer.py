import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_count = 0
    array_len = 20
    sub_matrix_len = int(np.sqrt(array_len))
    if sub_matrix_len ** 2 != array_len:
        return 0
    for i in range(len(matrix) - sub_matrix_len + 1):
        for j in range(len(matrix[0]) - sub_matrix_len + 1):
            sub_array = matrix[i:i + sub_matrix_len, j:j + sub_matrix_len]
            if len(sub_array) == sub_matrix_len ** 2:
                submatrices_count += 1
    return submatrices_count