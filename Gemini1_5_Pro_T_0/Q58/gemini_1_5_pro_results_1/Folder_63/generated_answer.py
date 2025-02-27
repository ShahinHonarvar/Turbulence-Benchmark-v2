import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 56):
        for j in range(cols - 56):
            submatrix = matrix[i:i + 57, j:j + 57]
            if submatrix.size == 57:
                count += 1
    return count