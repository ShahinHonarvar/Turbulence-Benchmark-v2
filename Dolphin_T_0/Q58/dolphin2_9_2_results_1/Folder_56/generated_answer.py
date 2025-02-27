import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(matrix_height - 2):
        for j in range(matrix_width - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 68:
                submatrix_count += 1
    return submatrix_count