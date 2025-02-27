import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for submatrix_rows in range(1, rows + 1):
        for submatrix_cols in range(1, cols + 1):
            if submatrix_rows * submatrix_cols == 77:
                for i in range(rows - submatrix_rows + 1):
                    for j in range(cols - submatrix_cols + 1):
                        submatrix = matrix[i:i + submatrix_rows, j:j + submatrix_cols]
                        submatrix_count += 1
    return submatrix_count