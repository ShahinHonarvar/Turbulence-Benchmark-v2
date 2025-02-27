import numpy as np

def submatrix_with_n_numbers(matrix):
    height = matrix.shape[0]
    width = matrix.shape[1]
    count = 0
    for i in range(height - 2):
        for j in range(width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == 27:
                count += 1
    return count