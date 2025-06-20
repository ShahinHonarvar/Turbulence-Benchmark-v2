import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 51
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix) == n:
                count += 1
    return count