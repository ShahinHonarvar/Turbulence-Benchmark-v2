import numpy as np

def submatrix_with_n_numbers(matrix, n=19):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == n:
                count += 1
    return count