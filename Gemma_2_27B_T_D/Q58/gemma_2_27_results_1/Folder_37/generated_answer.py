import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - 7):
        for j in range(cols - 7):
            if np.size(matrix[i:i + 8, j:j + 8]) == 64:
                count += 1
    return count