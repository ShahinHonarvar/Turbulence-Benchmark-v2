import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 3):
        for c in range(cols - 9):
            submatrix = matrix[r:r + 4, c:c + 10]
            if submatrix.size == 40:
                count += 1
    return count