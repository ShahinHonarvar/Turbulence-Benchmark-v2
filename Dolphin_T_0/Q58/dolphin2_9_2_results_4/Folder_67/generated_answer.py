import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            if matrix[i:i + 5, j:j + 5].flatten().size() == 43:
                count += 1
    return count