import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 159
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, np.array([n])).all():
                count += 1
    return count