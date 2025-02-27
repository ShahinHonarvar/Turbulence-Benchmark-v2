import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    target_count = 176
    count = 0
    for row in range(rows):
        for col in range(cols):
            for r in range(row + 1, rows + 1):
                for c in range(col + 1, cols + 1):
                    submatrix = matrix[row:r, col:c]
                    if np.size(submatrix) == target_count:
                        count += 1
    return count