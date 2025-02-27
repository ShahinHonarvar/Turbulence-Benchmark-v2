import numpy as np

def submatrix_with_n_numbers(matrix):

    def is_valid_matrix(submatrix):
        return len(submatrix) > 0 and len(submatrix[0]) > 0
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for submatrix_row in range(row + 1, rows + 1):
                for submatrix_col in range(col + 1, cols + 1):
                    submatrix = matrix[row:submatrix_row, col:submatrix_col]
                    if is_valid_matrix(submatrix) and submatrix.size == 34:
                        count += 1
    return count