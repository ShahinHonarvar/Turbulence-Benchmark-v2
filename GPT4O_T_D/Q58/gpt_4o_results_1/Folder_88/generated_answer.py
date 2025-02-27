import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_rows, submatrix_cols = (1, 67)
    count = 0
    while submatrix_rows * submatrix_cols <= 67:
        for i in range(rows - submatrix_rows + 1):
            for j in range(cols - submatrix_cols + 1):
                submatrix = matrix[i:i + submatrix_rows, j:j + submatrix_cols]
                if submatrix.size == 67:
                    count += 1
        submatrix_rows += 1
        if rows * submatrix_rows > 67:
            break
        submatrix_cols = 67 // submatrix_rows
    return count