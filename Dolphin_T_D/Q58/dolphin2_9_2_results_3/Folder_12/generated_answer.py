import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 3):
        for j in range(n - 3):
            if np.all(matrix[i:i + 4, j:j + 4] == 46):
                count += 1
    return count