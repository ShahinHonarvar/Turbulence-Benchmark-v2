import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    sub_matrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 3 < rows and j + 3 < cols:
                sub_matrix = matrix[i:i + 4, j:j + 4]
                if np.count_nonzero(sub_matrix) == 84:
                    sub_matrix_count += 1
    return sub_matrix_count