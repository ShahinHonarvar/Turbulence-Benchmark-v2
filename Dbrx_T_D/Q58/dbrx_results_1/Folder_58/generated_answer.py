import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 185, j:j + 185]
            if submatrix.shape == (185, 185) and np.isin(submatrix, 185).all():
                count += 1
    return count