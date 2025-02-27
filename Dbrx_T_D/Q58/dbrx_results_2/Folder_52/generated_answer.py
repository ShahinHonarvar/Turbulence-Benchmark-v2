import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n, m = matrix.shape
    for i in range(n - 2 + 1):
        for j in range(m - 2 + 1):
            submatrix = matrix[i:i + 3, j:j + 3]
            if (submatrix == 147).sum() == 9:
                submatrix_count += 1
    return submatrix_count