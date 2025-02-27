import numpy as np

def submatrix_with_n_numbers(matrix, n=49):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if np.sum(submatrix) == n:
                count += 1
    return count