import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == 111):
                count += 1
    return count