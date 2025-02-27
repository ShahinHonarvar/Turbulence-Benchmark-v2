import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    rows, cols = matrix.shape
    for i in range(rows - 11):
        for j in range(cols - 11):
            if np.count_nonzero(matrix[i:i + 12, j:j + 12]) == 68:
                total += 1
    return total