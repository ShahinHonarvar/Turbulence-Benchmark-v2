import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for k in range(1, min(n, m)):
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                if np.count_nonzero(matrix[i:i + k, j:j + k]) == 176:
                    count += 1
    return count