import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 96):
        for j in range(cols - 96):
            submatrix = matrix[i:i + 97, j:j + 97]
            if np.count_nonzero(submatrix) == 97:
                count += 1
    return count