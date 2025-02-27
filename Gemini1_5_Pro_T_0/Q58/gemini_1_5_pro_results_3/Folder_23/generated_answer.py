import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 68):
        for j in range(cols - 68):
            submatrix = matrix[i:i + 69, j:j + 69]
            if submatrix.size == 69:
                count += 1
    return count