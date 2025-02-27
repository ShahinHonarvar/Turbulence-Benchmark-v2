import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, n + 1):
                    if np.sum(matrix[i:k, j:l]) == 60:
                        count += 1
    return count