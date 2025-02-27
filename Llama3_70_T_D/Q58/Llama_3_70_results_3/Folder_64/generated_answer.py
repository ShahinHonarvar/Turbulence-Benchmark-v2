import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 7
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - 1):
        for col in range(cols - 1):
            submatrix = matrix[row:row + 2, col:col + 2].flatten()
            if len(submatrix) == n and len(np.unique(submatrix)) == n:
                count += 1
    return count