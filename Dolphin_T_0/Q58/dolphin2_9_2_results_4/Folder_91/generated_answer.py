import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 4 < rows and j + 4 < cols:
                submatrix = matrix[i:i + 5, j:j + 5]
                if submatrix.size == 25:
                    count += 1
    return count