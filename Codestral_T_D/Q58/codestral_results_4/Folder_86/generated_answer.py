import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 138
    shape = np.array(matrix.shape) - np.array([n, n]) + 1
    shape = shape.astype(int)
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n * 138:
                count += 1
    return count