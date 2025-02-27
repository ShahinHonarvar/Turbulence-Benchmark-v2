import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for submatrix_row in range(1, rows + 1):
        for submatrix_col in range(1, cols + 1):
            if submatrix_row * submatrix_col == 185:
                for i in range(rows - submatrix_row + 1):
                    for j in range(cols - submatrix_col + 1):
                        submatrix_count += 1
    return submatrix_count