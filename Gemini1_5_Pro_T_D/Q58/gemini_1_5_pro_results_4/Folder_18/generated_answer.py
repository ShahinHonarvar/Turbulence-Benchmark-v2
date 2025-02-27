import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 103):
        for j in range(cols - 103):
            submatrix = matrix[i:i + 104, j:j + 104]
            if submatrix.size == 104:
                count += 1
    return count