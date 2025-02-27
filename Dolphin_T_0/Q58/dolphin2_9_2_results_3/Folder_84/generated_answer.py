import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if 127 in matrix[i:i + 127, j:j + 127]:
                count += 1
    return count