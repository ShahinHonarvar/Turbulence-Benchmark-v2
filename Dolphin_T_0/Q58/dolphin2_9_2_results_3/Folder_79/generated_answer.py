import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 11):
        for j in range(n - 11):
            submatrix = matrix[i:i + 12, j:j + 12]
            if np.count_nonzero(submatrix) == 60:
                count += 1
    return count