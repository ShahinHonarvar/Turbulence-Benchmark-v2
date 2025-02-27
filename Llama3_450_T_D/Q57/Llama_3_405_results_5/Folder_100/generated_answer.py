import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for row_size in range(1, rows - row + 1):
                for col_size in range(1, cols - col + 1):
                    submatrix = matrix[row:row + row_size, col:col + col_size]
                    if np.sum(submatrix) == 28:
                        result.append(submatrix)
    return result