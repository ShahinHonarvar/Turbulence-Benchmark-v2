import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 9:
                count += 1
    return count