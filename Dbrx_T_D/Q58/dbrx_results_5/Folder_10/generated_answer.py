import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 1):
        for j in range(m - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.all(np.equal(submatrix, 56)):
                count += 1
    return count