import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices = 0
    rows, cols = matrix.shape
    for i in range(rows - 4):
        for j in range(cols - 5):
            if np.count_nonzero(matrix[i:i + 5, j:j + 5] == 48) == 25:
                submatrices += 1
    return submatrices