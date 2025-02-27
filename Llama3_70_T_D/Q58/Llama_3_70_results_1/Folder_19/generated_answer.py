import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 3):
        for col in range(cols - 3):
            count += np.sum(matrix[row:row + 4, col:col + 4]) == 17
            for i in range(1, 4):
                count += np.sum(matrix[row:row + 4, col:col + 4 - i]) == 17
                count += np.sum(matrix[row:row + 4 - i, col:col + 4]) == 17
    return count