import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if np.size(submatrix) == 48:
                count += 1
    return count