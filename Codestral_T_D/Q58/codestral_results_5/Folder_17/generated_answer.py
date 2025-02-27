import numpy as np

def submatrix_with_n_numbers(matrix, n=166):
    rows, cols = matrix.shape
    count = 0
    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for row_start in range(rows - row_size + 1):
                for col_start in range(cols - col_size + 1):
                    submatrix = matrix[row_start:row_start + row_size, col_start:col_start + col_size]
                    if np.sum(submatrix == 166) == n:
                        count += 1
    return count