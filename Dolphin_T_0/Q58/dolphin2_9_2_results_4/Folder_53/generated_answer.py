import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i:i + 2, j:j + 2].size == 24:
                count += 1
    return count if count else 0