import numpy as np

def submatrix_with_n_numbers(matrix):
    x_length, y_length = matrix.shape
    count = 0
    for x in range(x_length - 2):
        for y in range(y_length - 2):
            if np.count_nonzero(matrix[x:x + 3, y:y + 3]) == 33:
                count += 1
    return count