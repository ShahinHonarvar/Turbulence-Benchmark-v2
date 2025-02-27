import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 7 + 1):
        for col in range(cols - 6 + 1):
            if np.sum(matrix[row:row + 8, col:col + 6]) == 48 * 8:
                count += 1
    return count