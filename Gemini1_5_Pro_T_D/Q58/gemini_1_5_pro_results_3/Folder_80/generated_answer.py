import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 179):
        for j in range(cols - 179):
            submatrix = matrix[i:i + 180, j:j + 180]
            if submatrix.size == 180 * 180:
                count += 1
    return count