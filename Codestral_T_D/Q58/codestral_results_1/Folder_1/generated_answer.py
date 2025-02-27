import numpy as np

def submatrix_with_n_numbers(matrix):
    target_sum = 23
    n = 2
    row, col = matrix.shape
    count = 0
    for i in range(row - n + 1):
        for j in range(col - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == target_sum:
                count += 1
    return count