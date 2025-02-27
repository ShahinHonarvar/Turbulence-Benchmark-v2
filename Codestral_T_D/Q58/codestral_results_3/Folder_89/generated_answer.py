import numpy as np

def submatrix_with_n_numbers(matrix, n=18):
    rows, cols = matrix.shape
    submatrices = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.count_nonzero(submatrix) == n:
                submatrices += 1
    return submatrices