import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i:i + sqrt(21), j:j + sqrt(21)].size == 21:
                count += 1
    return count