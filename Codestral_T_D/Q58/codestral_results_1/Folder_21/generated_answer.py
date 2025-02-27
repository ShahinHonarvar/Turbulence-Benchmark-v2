import numpy as np

def submatrix_with_n_numbers(matrix, n=139):
    rows, cols = matrix.shape
    count = 0
    for row_len in range(1, rows + 1):
        for col_len in range(1, cols + 1):
            for row_start in range(rows - row_len + 1):
                for col_start in range(cols - col_len + 1):
                    submatrix = matrix[row_start:row_start + row_len, col_start:col_start + col_len]
                    if submatrix.size == n and np.all(submatrix == 139):
                        count += 1
    return count