import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows - 4):
        for j in range(cols - 4):
            if np.count_nonzero(matrix[i:i + 5, j:j + 5]) == 20:
                counter += 1
    return counter