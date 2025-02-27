import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    if np.count_nonzero(matrix[i:k + 1, j:l + 1]) == 131:
                        count += 1
    return count