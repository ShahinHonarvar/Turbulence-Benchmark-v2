import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - 11):
        for j in range(cols - 11):
            submatrix = matrix[i:i + 12, j:j + 12]
            if np.count_nonzero(submatrix) == 144:
                count += 1
    return count