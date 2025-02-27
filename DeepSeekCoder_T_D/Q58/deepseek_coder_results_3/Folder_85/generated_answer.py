import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 12):
        for c in range(cols - 12):
            submatrix = matrix[r:r + 13, c:c + 13]
            if submatrix.size == 169:
                count += 1
    return count