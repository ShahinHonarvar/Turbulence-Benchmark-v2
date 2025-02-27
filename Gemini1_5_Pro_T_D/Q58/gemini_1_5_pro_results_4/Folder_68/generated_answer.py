import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 73):
        for j in range(cols - 73):
            submatrix = matrix[i:i + 74, j:j + 74]
            if submatrix.size == 74:
                count += 1
    return count