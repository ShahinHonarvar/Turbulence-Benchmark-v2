import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            if r + 2 < rows and c + 2 < cols:
                submatrix = matrix[r:r + 3, c:c + 3]
                if submatrix.size == 9:
                    count += 1
            if r + 1 < rows and c + 6 < cols:
                submatrix = matrix[r:r + 2, c:c + 7]
                if submatrix.size == 14:
                    count += 1
            if r + 6 < rows and c + 1 < cols:
                submatrix = matrix[r:r + 7, c:c + 2]
                if submatrix.size == 14:
                    count += 1
            if r + 1 < rows and c + 3 < cols:
                submatrix = matrix[r:r + 2, c:c + 4]
                if submatrix.size == 8:
                    count += 1
            if r + 3 < rows and c + 1 < cols:
                submatrix = matrix[r:r + 4, c:c + 2]
                if submatrix.size == 8:
                    count += 1
    return count