import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == 49:
                count += 1
    return count