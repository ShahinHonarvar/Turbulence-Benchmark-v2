import numpy as np

def submatrix_with_n_numbers(matrix, n=180):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + n - 1 < rows and c + n - 1 < cols:
                submatrix = matrix[r:r + n, c:c + n]
                if np.sum(submatrix) == n * 180:
                    count += 1
    return count