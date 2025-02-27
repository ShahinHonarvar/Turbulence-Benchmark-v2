import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 10):
        for j in range(matrix.shape[1] - 10):
            submatrix = matrix[i:i + 11, j:j + 11]
            if np.size(submatrix) == 121:
                count += 1
    return count