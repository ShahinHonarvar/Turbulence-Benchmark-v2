import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 131
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + n // cols, min(rows, i + n // cols + 1)):
                for l in range(j + n % cols, min(cols, j + n % cols + 1)):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == n:
                        count += 1
    return count