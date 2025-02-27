import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 180
    rows, cols = matrix.shape
    if rows * cols != n:
        return 0
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + n // rows < rows and c + n // cols < cols:
                submatrix = matrix[r:r + n // rows, c:c + n // cols]
                if np.all(submatrix.reshape(-1) != 0):
                    count += 1
    return count