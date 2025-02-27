import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 33
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - n // cols + 1):
        for j in range(cols - n % cols + 1):
            if np.sum(matrix[i:i + n // cols, j:j + n % cols]) == n:
                count += 1
    return count