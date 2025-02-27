import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    if np.count_nonzero(matrix[i:k + 1, j:l + 1]) == 138:
                        count += 1
    if count == 0:
        return 0
    else:
        return count