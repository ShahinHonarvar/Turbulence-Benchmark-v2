import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 5 + 1):
        for j in range(n - 6 + 1):
            if 56 in np.array(matrix[i:i + 5, j:j + 6]):
                count += 1
    return count