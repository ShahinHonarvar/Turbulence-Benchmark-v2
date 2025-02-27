import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 1:
                for r in range(row, rows):
                    for c in range(col, cols):
                        submatrix = matrix[row:r + 1, col:c + 1]
                        if np.sum(submatrix) == 1:
                            count += 1
    return count