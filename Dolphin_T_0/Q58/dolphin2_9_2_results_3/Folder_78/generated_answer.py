import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0] * matrix.shape[1]
    if n == 0:
        return 0
    submatrix_count = 0
    for i in range(0, matrix.shape[0]):
        for j in range(0, matrix.shape[1]):
            if i + 13 <= matrix.shape[0] and j + 13 <= matrix.shape[1]:
                num_count = 0
                for r in range(i, i + 13):
                    for c in range(j, j + 13):
                        num_count += matrix[r, c]
                if num_count == 91:
                    submatrix_count += 1
    return submatrix_count