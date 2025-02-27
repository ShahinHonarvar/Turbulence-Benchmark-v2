import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    num_submatrices = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, [20]).any():
                num_submatrices += 1
    return num_submatrices