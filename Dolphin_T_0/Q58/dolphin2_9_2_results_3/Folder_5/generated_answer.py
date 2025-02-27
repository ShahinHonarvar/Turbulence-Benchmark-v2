import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    number_of_submatrices = 0
    for i in range(shape[0] - 7):
        for j in range(shape[1] - 7):
            is_submatrix = False
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.all(submatrix == 63):
                is_submatrix = True
            if is_submatrix:
                number_of_submatrices += 1
    return number_of_submatrices