import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 47 + 1):
        for j in range(cols - 47 + 1):
            submatrix = matrix[i:i + 47, j:j + 47]
            if submatrix.size == 47:
                count += 1
    return count