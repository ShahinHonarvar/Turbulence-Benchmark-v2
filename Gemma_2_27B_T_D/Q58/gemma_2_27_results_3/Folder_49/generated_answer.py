import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 8 + 1):
        for j in range(cols - 8 + 1):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.count_nonzero(submatrix) == 72:
                count += 1
    return count