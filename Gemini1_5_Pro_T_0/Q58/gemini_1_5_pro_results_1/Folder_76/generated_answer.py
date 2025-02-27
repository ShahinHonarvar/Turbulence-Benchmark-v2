import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 158):
        for j in range(cols - 158):
            submatrix = matrix[i:i + 159, j:j + 159]
            if submatrix.size == 159:
                count += 1
    return count