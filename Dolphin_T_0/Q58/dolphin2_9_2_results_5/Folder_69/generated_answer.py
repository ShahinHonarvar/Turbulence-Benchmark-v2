import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 126
    shape = matrix.shape
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            sub_matrix = matrix[i:i + n, j:j + n]
            if sub_matrix.size == n:
                count += 1
    return count