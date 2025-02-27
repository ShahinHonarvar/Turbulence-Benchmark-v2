import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 10):
        for c in range(cols - 10):
            submatrix = matrix[r:r + 11, c:c + 11]
            if submatrix.size == 121:
                count += 1
    return count