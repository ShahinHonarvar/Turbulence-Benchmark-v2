import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n - 3):
        for j in range(n - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.sum() == 34 * 4 * 4:
                count += 1
    return count