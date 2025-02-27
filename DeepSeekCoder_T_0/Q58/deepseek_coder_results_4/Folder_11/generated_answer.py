import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for i in range(r + 1, rows + 1):
                for j in range(c + 1, cols + 1):
                    submatrix = matrix[r:i, c:j]
                    if submatrix.size == 38:
                        count += 1
    return count