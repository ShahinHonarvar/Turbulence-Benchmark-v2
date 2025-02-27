import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if len(submatrix.flatten()) == 56:
                counter += 1
    return counter