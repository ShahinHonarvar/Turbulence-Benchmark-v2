import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for r in range(rows - 15):
        for c in range(cols - 12):
            if np.all(matrix[r:r + 16, c:c + 12] == matrix[r:r + 16, c:c + 12].T):
                count += 1
    return count