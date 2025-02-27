import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 120):
        for j in range(cols - 120):
            submatrix = matrix[i:i + 121, j:j + 121]
            if submatrix.size == 121 * 121:
                count += 1
    return count