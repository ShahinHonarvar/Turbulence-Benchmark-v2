import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 66
    m, l = matrix.shape
    count = 0
    for i in range(m):
        for j in range(l):
            if i + n - 1 < m and j + n - 1 < l:
                submatrix = matrix[i:i + n, j:j + n]
                if np.count_nonzero(submatrix == 66) == n:
                    count += 1
    return count