import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2 + 1):
        for j in range(cols - 23 + 1):
            submatrix = matrix[i:i + 2, j:j + 23]
            if np.isin(submatrix, [23]).all():
                count += 1
    return count