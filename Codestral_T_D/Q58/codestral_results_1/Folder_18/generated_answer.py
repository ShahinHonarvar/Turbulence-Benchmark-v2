import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 104
    if rows * cols < n:
        return 0
    for row in range(rows - n + 1):
        for col in range(cols - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if np.sum(submatrix == 104) == n:
                count += 1
    return count