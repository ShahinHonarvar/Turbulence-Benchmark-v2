import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 2, j:j + 3]
            if len(submatrix.flatten()) == 8:
                count += 1
    return count