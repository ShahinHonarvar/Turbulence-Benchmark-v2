import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(matrix.shape[0] - i):
                for l in range(matrix.shape[1] - j):
                    if matrix[i:i + k + 1, j:j + l + 1].size == 23:
                        count += 1
    return count