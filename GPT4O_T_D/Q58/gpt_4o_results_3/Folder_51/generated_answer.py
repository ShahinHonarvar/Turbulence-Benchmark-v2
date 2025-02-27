import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 10 or cols < 10:
        return 0
    count = 0
    for i in range(rows - 9):
        for j in range(cols - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if submatrix.size == 100:
                count += 1
    return count