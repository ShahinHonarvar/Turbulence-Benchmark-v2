import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + 5 < rows and c + 5 < cols:
                submatrix = matrix[r:r + 6, c:c + 6]
                if np.count_nonzero(submatrix) == 54:
                    count += 1
    return count