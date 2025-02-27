import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 6):
        for j in range(m - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.sum() == 185 * 7 * 7:
                count += 1
    return count