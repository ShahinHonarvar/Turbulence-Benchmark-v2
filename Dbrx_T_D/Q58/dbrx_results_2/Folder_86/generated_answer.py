import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2 + 1):
        for j in range(cols - 2 + 1):
            submatrix = matrix[i:i + 3, j:j + 3]
            if 138 in submatrix:
                submatrix_count += 1
    return submatrix_count