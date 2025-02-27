import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows - 1):
        for col_start in range(cols - 1):
            submatrix = matrix[row_start:, col_start:]
            if submatrix.size >= 49 and np.all(submatrix == 49):
                count += 1
    return count