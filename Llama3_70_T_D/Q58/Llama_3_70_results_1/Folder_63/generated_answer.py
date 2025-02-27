import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for row_end in range(row + 1, matrix.shape[0] + 1):
                for col_end in range(col + 1, matrix.shape[1] + 1):
                    submatrix = matrix[row:row_end, col:col_end]
                    if submatrix.size == 57:
                        count += 1
    return count