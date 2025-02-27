import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    n = 3
    counter = 0
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            if len(set(matrix[i:i + n, j:j + n].flatten())) == n * n:
                counter += 1
    return counter