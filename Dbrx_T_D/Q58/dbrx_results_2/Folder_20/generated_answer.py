import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    return sum((np.sum(submatrix) == 49 * n for i in range(rows - n + 1) for j in range(cols - n + 1) for submatrix in (matrix[i:i + n, j:j + n],)))