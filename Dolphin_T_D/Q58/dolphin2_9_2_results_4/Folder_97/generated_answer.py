import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 11):
        for j in range(col - 11):
            if np.count_nonzero(matrix[i:i + 12, j:j + 12]) == 120:
                count += 1
    return count