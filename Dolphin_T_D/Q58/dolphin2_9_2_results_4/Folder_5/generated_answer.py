import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 8 < rows and j + 8 < cols) and len(set(matrix[i:i + 9, j:j + 9].flatten())) == 63:
                count += 1
    return count