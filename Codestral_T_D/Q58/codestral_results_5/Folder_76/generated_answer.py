import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i, n_rows):
                for l in range(j, n_cols):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 159 * ((k - i + 1) * (l - j + 1)):
                        count += 1
    return count