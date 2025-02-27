import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 176
    m, k = matrix.shape
    count = 0
    for i in range(m):
        for j in range(k):
            for x in range(i, m):
                for y in range(j, k):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == n:
                        count += 1
    return count