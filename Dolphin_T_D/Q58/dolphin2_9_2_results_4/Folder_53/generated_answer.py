import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrix = 0
    total_elements = matrix.shape[0] * matrix.shape[1]
    if total_elements < 24:
        return 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 5):
            submatrix = matrix[i:i + 5, j:j + 5]
            if np.count_nonzero(submatrix == 24) == 25:
                num_submatrix += 1
    return num_submatrix