import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 11):
        for j in range(n - 11):
            if np.count_nonzero(matrix[i:i + 12, j:j + 12]) == 185:
                count += 1
    return count