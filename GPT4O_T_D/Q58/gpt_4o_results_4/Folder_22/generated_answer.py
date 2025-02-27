import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 7 or cols < 3:
        return 0
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 7, j:j + 3]
            if submatrix.size == 21:
                count += 1
    return count