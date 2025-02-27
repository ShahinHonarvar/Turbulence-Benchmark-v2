import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 6 <= rows and j + 5 <= cols:
                submatrix = matrix[i:i + 7, j:j + 6]
                if submatrix.size == 40:
                    count += 1
    return count