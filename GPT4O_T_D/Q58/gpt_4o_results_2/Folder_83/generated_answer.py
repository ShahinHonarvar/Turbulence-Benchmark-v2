import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r + 1, rows + 1):
                for c2 in range(c + 1, cols + 1):
                    submatrix = matrix[r:r2, c:c2]
                    if submatrix.size == 47:
                        submatrix_count += 1
    return submatrix_count