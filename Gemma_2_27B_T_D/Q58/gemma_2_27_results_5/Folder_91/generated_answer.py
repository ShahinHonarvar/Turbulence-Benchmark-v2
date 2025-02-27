import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if np.prod(matrix[i:k + 1, j:l + 1].shape) == 25:
                        count += 1
    return count