import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(submatrix, 104).all():
                num_submatrices += 1
    return num_submatrices