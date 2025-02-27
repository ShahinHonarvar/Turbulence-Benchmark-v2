import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 186
    for row in range(rows):
        for col in range(cols):
            max_row = min(row + int(np.ceil(np.sqrt(n))), rows)
            max_col = min(col + int(np.ceil(np.sqrt(n))), cols)
            for r in range(row, max_row + 1):
                for c in range(col, max_col + 1):
                    submatrix = matrix[row:r, col:c]
                    if submatrix.size == n:
                        count += 1
    return count