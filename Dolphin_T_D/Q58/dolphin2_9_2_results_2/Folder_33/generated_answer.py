import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            if matrix[i:i + 2, j:j + 2].size == 118:
                count += 1
    return count