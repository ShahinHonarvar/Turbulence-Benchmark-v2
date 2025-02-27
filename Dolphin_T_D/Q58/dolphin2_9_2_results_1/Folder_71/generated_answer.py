import numpy as np

def submatrix_with_n_numbers(matrix):
    size = 78
    rows, cols = matrix.shape
    submatrices = 0
    for i in range(0, rows - size + 1):
        for j in range(0, cols - size + 1):
            if np.count_nonzero(matrix[i:i + size, j:j + size]) == size:
                submatrices += 1
    return submatrices