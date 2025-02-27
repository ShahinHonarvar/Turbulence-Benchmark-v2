import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 4 + 1):
        for j in range(matrix.shape[1] - 4 + 1):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.count_nonzero(submatrix) == 40:
                count += 1
    return count