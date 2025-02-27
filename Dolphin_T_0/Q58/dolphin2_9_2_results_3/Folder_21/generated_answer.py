import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 139
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if sum(matrix[i:i + n_numbers, j:j + n_numbers]) == n_numbers:
                count += 1
    return count