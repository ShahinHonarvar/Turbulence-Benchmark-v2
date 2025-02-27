import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m):
        for j in range(n):
            if i + 2 < m and j + 3 < n:
                counter_sub = np.count_nonzero(matrix[i:i + 3, j:j + 4] == 74)
                if counter_sub >= 74:
                    counter += 1
    return counter