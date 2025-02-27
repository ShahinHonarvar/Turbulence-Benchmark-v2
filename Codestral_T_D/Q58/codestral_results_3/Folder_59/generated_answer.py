import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 76
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + n, rows + 1):
                for l in range(j + n, cols + 1):
                    if np.count_nonzero(matrix[i:k, j:l] == 76) == n:
                        count += 1
    return count