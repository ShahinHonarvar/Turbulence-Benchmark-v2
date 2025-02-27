import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 117):
        for j in range(cols - 117):
            submatrix = matrix[i:i + 118, j:j + 118]
            if submatrix.size == 118 * 118:
                count += 1
    return count