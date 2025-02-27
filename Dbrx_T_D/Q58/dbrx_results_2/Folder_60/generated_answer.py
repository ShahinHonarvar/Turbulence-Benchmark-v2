import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 8 + 1):
        for j in range(matrix.shape[1] - 8 + 1):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.isin(submatrix, 88).all():
                count += 1
    return count