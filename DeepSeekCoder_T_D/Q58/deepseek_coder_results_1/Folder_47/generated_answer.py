import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 8):
        for j in range(cols - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if submatrix.size == 81:
                count += 1
    return count