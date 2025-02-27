import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 20):
        for j in range(cols - 20):
            submatrix = matrix[i:i + 21, j:j + 21]
            if submatrix.size == 441:
                count += 1
    return count