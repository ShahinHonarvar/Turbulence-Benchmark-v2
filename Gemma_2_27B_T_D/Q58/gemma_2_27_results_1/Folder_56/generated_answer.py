import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.prod(matrix[i:k + 1, j:l + 1].shape) == 68:
                        count += 1
    return count