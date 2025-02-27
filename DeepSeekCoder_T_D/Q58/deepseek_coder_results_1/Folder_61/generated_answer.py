import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            if len(set(matrix[i:i + 2, j:j + 2].flatten())) == 4:
                count += 1
    return count