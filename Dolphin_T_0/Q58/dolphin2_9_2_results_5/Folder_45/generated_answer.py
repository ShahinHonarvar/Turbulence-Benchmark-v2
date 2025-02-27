import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape[0]
    for row in range(matrix_size):
        for col in range(matrix_size):
            for submatrix_size in range(2, matrix_size + 1):
                if row + submatrix_size - 1 < matrix_size and col + submatrix_size - 1 < matrix_size:
                    submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
                    if len(submatrix) == 28:
                        count += 1
    return count