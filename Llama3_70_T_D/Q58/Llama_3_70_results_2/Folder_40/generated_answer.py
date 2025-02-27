import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row1 in range(rows):
        for col1 in range(cols):
            for row2 in range(row1, rows):
                for col2 in range(col1, cols):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if np.count_nonzero(submatrix == 1) == 1:
                        count += 1
    return count