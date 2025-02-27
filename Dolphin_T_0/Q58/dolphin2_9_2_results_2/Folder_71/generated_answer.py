import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(0, n):
        for j in range(0, m):
            if np.count_nonzero(matrix[i:i + 2, j:j + 2]) == 4:
                count += 1
    return count