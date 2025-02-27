import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0] - 9):
        for j in range(matrix.shape[1] - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.isin(submatrix, 60).sum() == 100:
                submatrix_count += 1
    return submatrix_count