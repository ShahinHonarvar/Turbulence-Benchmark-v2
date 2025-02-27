import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target = 84
    count = 0
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if submatrix.size == target:
                        count += 1
    return count