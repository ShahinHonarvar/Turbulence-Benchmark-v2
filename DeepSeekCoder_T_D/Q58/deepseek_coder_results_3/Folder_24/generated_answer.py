import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 4):
        for c in range(cols - 4):
            submatrix = matrix[r:r + 5, c:c + 5]
            if submatrix.size == 51:
                count += 1
    return count