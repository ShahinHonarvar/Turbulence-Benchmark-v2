import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - 5 + 1):
        for j in range(cols - 5 + 1):
            submatrix = matrix[i:i + 5, j:j + 5]
            if submatrix.size == 29:
                count += 1
    return count