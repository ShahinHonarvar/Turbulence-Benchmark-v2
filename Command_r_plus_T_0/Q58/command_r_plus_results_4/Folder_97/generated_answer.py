import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 119):
        for j in range(cols - 119):
            submatrix = matrix[i:i + 120, j:j + 120]
            if submatrix.size == 120 * 120:
                count += 1
    return count