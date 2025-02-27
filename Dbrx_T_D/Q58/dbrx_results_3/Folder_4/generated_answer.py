import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 15 or cols < 15:
        return 0
    count = 0
    for i in range(rows - 14):
        for j in range(cols - 14):
            submatrix = matrix[i:i + 15, j:j + 15]
            if np.isin(submatrix, 15).all():
                count += 1
    return count