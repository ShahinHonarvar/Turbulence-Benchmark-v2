import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 7
    m, _ = matrix.shape
    if m < n:
        return 0
    submatrices_with_n_numbers = 0
    for i in range(m - n + 1):
        for j in range(m - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 7):
                submatrices_with_n_numbers += 1
    return submatrices_with_n_numbers