import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    if rows >= 3 and cols >= 3:
        for i in range(rows - 2):
            for j in range(cols - 2):
                submatrix = matrix[i:i + 3, j:j + 3]
                if submatrix.size == 9:
                    submatrix_count += 1
    return submatrix_count