import numpy as np

def submatrix_with_n_numbers(matrix, n=21):
    shape = matrix.shape
    count = 0
    for i in range(shape[0] - n + 1):
        for j in range(shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix) == n:
                count += 1
    return count