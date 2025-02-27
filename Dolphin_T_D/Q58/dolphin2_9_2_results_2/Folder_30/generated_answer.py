import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 93):
        for j in range(n - 93):
            if np.all(matrix[i:i + 94, j:j + 94] == 94):
                count += 1
    return count