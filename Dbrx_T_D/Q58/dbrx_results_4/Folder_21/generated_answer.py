import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 2 + 1):
        for j in range(m - 2 + 1):
            submatrix = matrix[i:i + 2, j:j + 3]
            if np.count_nonzero(submatrix == 139) == 139:
                count += 1
    return count