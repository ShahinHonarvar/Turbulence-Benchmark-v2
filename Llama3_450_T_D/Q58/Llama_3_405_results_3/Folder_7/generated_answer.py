import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for r in range(row + 11, rows + 1):
                for c in range(col + 11, cols + 1):
                    submatrix = matrix[row:r, col:c]
                    if np.size(submatrix) == 121:
                        count += 1
    return count