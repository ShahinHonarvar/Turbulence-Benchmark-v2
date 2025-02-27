import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 4 < rows and j + 6 < cols:
                submatrix = matrix[i:i + 5, j:j + 7]
                if len(submatrix) == 84:
                    count += 1
    return count