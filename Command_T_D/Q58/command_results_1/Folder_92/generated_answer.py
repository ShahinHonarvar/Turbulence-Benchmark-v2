import numpy as np

def submatrix_with_n_numbers(matrix):
    count = np.sum((np.sum(matrix[i:i + 8, j:j + 8] == 8, axis=1) == 8 for i in range(0, len(matrix), 8)))
    return count