import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 4 + 1):
        for j in range(cols - 4 + 1):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.all(submatrix >= 0):
                count += 1
    return count