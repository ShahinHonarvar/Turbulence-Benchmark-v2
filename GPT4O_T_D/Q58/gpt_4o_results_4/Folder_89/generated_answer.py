import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            if r + 3 <= rows and c + 6 <= cols:
                submat = matrix[r:r + 3, c:c + 6]
                if submat.size == 18:
                    count += 1
            if r + 6 <= rows and c + 3 <= cols:
                submat = matrix[r:r + 6, c:c + 3]
                if submat.size == 18:
                    count += 1
    return count