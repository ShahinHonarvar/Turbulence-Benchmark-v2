import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    m, n = matrix.shape
    submatrix_count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix == 15) == 9:
                submatrix_count += 1
    return submatrix_count