import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i + 3, n_rows + 1):
                for l in range(j + 3, n_cols + 1):
                    if np.size(matrix[i:k, j:l]) == 33 and np.count_nonzero(matrix[i:k, j:l] == 33) == 33:
                        count += 1
    return count