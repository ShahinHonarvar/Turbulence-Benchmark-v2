import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if np.all(matrix[i:k, j:l] == 87):
                        submatrix_count += 1
    return submatrix_count