import numpy as np

def submatrix_with_n_numbers(matrix, n=76):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + n <= rows and c + n <= cols:
                submatrix = matrix[r:r + n, c:c + n]
                if np.count_nonzero(submatrix == 76) == n:
                    count += 1
    return count