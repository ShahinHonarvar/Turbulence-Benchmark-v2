import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows - 2):
        for col in range(cols - 2):
            if np.sum(matrix[row:row + 3, col:col + 3]) == 111:
                count += 1
    return count