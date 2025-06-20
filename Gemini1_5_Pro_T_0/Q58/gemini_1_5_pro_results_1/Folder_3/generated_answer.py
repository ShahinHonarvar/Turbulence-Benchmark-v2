import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 53):
        for j in range(cols - 53):
            submatrix = matrix[i:i + 54, j:j + 54]
            if submatrix.size == 54 * 54:
                count += 1
    return count