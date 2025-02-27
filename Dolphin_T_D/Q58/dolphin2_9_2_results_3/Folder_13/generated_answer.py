import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 175
    m = len(matrix)
    k = len(matrix[0])
    for i in range(m - n + 1):
        for j in range(k - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == n):
                submatrix_count += 1
    return submatrix_count