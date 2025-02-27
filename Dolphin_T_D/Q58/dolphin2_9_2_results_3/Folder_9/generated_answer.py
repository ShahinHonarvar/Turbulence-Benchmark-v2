import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 33
    shape = matrix.shape
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i + n_numbers <= shape[0] and j + n_numbers <= shape[1]:
                submatrix = matrix[i:i + n_numbers, j:j + n_numbers]
                if np.count_nonzero(submatrix) == n_numbers:
                    count += 1
    return count