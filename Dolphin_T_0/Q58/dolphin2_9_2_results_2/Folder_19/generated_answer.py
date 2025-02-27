import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 17
    matrix = np.array(matrix)
    h = len(matrix)
    w = len(matrix[0])
    count = 0
    for i in range(h - n + 1):
        for j in range(w - n + 1):
            if np.all(matrix[i:i + n, j:j + n] == matrix[i:i + n, j:j + n][0, 0]) and np.all(matrix[i:i + n, j:j + n] == matrix[i:i + n, j:j + n][n - 1, n - 1]) and np.all(matrix[i:i + n, j:j + n] == matrix[i:i + n, j:j + n][:, 0]) and np.all(matrix[i:i + n, j:j + n] == matrix[i:i + n, j:j + n][:, n - 1]):
                count += 1
    return count