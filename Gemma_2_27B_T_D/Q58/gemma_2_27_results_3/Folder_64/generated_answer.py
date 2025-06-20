import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.size(submatrix) == 9:
                count += 1
    return count