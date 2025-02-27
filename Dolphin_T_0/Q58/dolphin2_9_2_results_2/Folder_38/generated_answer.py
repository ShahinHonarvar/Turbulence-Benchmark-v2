import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for left in range(cols - 1):
        for up in range(rows - 1):
            for right in range(left + 1, cols):
                for down in range(up + 1, rows):
                    if len(np.unique(matrix[up:down + 1, left:right + 1])) == 34:
                        count += 1
    return count