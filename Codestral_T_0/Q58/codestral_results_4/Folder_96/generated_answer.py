import numpy as np

def submatrix_with_n_numbers(matrix, n=20):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 4):
        for j in range(cols - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if np.sum(submatrix) == n:
                count += 1
    return count