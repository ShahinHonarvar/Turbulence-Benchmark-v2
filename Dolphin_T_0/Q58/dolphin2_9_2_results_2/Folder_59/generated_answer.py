import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 76
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns - n + 1):
            if np.all(matrix[i, j:j + n] >= 0):
                count += 1
    for i in range(rows - n + 1):
        for j in range(columns):
            if np.all(matrix[i:i + n, j] >= 0):
                count += 1
    if count > 0:
        return count
    else:
        return 0