import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 8 <= rows and j + 8 <= cols:
                submatrix = matrix[i:i + 9, j:j + 9]
                if submatrix.size == 72:
                    count += 1
    return count