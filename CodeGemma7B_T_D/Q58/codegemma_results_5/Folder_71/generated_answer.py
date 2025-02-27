import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for r in range(row, matrix.shape[0]):
                for c in range(col, matrix.shape[1]):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if submatrix.shape[0] * submatrix.shape[1] == 78:
                        submatrix_count += 1
    return submatrix_count