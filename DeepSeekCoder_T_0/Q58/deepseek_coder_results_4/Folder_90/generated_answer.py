import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 16):
        for c in range(cols - 9):
            submatrix = matrix[r:r + 17, c:c + 10]
            if submatrix.size == 176:
                count += 1
    return count