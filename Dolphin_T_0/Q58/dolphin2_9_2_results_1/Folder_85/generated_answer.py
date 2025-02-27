import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix == 13) == 9:
                count += 1
    return count