import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n, m = matrix.shape
    for i in range(n - 3):
        for j in range(m - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.count_nonzero(submatrix == 8) == 8:
                submatrix_count += 1
    return submatrix_count