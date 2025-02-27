import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_rows, matrix_cols = matrix.shape
    count = 0
    for r in range(matrix_rows):
        for c in range(matrix_cols):
            for height in range(1, matrix_rows - r + 1):
                for width in range(1, matrix_cols - c + 1):
                    if height * width == 54:
                        submatrix = matrix[r:r + height, c:c + width]
                        if submatrix.size == 54:
                            count += 1
    return count