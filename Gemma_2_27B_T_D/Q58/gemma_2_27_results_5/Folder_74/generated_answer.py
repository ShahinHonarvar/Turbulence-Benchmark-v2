import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 6 <= rows and j + 7 <= cols:
                submatrix = matrix[i:i + 7, j:j + 7]
                if submatrix.size == 48:
                    count += 1
    return count