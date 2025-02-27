import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 39):
        for j in range(cols - 39):
            submatrix = matrix[i:i + 40, j:j + 40]
            if np.count_nonzero(submatrix) == 40:
                count += 1
    return count