import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_size = len(matrix)
    if matrix_size < 10:
        return submatrix_count
    for i in range(matrix_size - 9):
        for j in range(matrix_size - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.all(submatrix == 80):
                submatrix_count += 1
    return submatrix_count