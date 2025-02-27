import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 175):
        for j in range(cols - 175):
            submatrix = matrix[i:i + 176, j:j + 176]
            if submatrix.size == 176:
                count += 1
    return count