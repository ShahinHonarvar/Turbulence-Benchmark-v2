import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0] - 29 + 1):
        for j in range(shape[1] - 29 + 1):
            submatrix = matrix[i:i + 29, j:j + 29]
            if np.all(submatrix == 29):
                count += 1
    return count