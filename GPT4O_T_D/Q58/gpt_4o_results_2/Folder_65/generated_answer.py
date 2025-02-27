import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for r in range(rows):
        for c in range(cols):
            for nr in range(r + 1, rows + 1):
                for nc in range(c + 1, cols + 1):
                    submatrix = matrix[r:nr, c:nc]
                    if submatrix.size == 35:
                        submatrix_count += 1
    return submatrix_count