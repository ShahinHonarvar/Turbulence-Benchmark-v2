import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 97
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n ** 2:
                count += 1
    if count == 0:
        return 0
    else:
        return count