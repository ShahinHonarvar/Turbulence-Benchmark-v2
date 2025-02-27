import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] == 0:
                if r + 9 < rows and c + 9 < cols:
                    submatrix = matrix[r:r + 10, c:c + 10]
                    if np.all(submatrix == 99):
                        count += 1
    return count