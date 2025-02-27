import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            submatrix = matrix[i:n, j:m]
            if submatrix.size >= 92 and np.count_nonzero(submatrix == 42) == 92:
                count += 1
    return count