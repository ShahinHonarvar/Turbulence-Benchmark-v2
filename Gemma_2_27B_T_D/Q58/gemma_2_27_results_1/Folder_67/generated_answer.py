import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 43
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n // cols <= rows and j + n % cols <= cols:
                submatrix = matrix[i:i + n // cols, j:j + n % cols].flatten()
                if len(submatrix) == n:
                    count += 1
    return count