import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 4 + 1):
        for j in range(cols - 4 + 1):
            if np.count_nonzero(matrix[i:i + 4, j:j + 4]) == 96:
                count += 1
    return count