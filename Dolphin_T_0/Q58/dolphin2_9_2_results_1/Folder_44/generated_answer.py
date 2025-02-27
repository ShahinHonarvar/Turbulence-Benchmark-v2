import numpy as np

def submatrix_with_n_numbers(matrix):
    m = np.sum(matrix, axis=None)
    if m % 191 == 0:
        count = 0
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if sum(matrix[i:i + 191, j:j + 191]) == 191:
                    count += 1
        return count
    return 0