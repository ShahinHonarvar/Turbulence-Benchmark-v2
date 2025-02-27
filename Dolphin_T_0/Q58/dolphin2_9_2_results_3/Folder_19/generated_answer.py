import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 16):
        for j in range(cols - 16):
            submatrix = matrix[i:i + 17, j:j + 17]
            if len(submatrix.flatten()) == 17:
                count += 1
    return count