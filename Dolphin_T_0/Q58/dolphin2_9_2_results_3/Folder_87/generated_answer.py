import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 9):
        for c in range(cols - 9):
            if np.all(matrix[r:r + 10, c:c + 10] == 96):
                count += 1
    return count