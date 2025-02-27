import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    submatrix = matrix[i:r, j:c]
                    if submatrix.size == 40:
                        counter += 1
    return counter