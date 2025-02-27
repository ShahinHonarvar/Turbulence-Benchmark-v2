import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_rows = matrix.shape[0]
    matrix_cols = matrix.shape[1]
    for i in range(matrix_rows - 2):
        for j in range(matrix_cols - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if len(sub_matrix) == 3 and len(sub_matrix[0]) == 3:
                if len(sub_matrix.flatten()) == 9 and (not np.isnan(sub_matrix).any()):
                    count += 1
    return count