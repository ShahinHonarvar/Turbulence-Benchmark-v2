import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 18 // cols <= rows and j + 18 % cols == 0:
                submatrix = matrix[i:i + 18 // cols, j:j + 18 % cols]
                if submatrix.size == 180:
                    count += 1
    return count