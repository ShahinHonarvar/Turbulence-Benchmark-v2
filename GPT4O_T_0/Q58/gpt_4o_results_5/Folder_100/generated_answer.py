import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + 1 < rows and c + 4 < cols:
                submatrix = matrix[r:r + 2, c:c + 5]
                if submatrix.size == 10:
                    count += 1
            if r + 4 < rows and c + 1 < cols:
                submatrix = matrix[r:r + 5, c:c + 2]
                if submatrix.size == 10:
                    count += 1
    return count