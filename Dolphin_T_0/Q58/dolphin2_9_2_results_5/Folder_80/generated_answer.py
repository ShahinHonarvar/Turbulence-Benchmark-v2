import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 180
    for i in range(rows):
        for j in range(cols):
            if matrix[i:i + n] and matrix[:, j:j + n]:
                count += 1
    return count if count else 0