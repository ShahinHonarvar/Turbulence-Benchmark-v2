import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + 2 < matrix.shape[0] and j + 2 < matrix.shape[1]:
                submatrix = matrix[i:i + 3, j:j + 3]
                if np.count_nonzero(submatrix) == 191:
                    count += 1
    return count