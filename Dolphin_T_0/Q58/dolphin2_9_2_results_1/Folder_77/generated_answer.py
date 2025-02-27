import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 178):
        for j in range(cols - 178):
            if np.sum(matrix[i:i + 179, j:j + 179]) == 179 * 179:
                count += 1
    return count