import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            if i + 6 < rows and j + 6 < cols:
                submatrix = matrix[i:i + 7, j:j + 7]
                if submatrix.size == 46:
                    count += 1
    return count