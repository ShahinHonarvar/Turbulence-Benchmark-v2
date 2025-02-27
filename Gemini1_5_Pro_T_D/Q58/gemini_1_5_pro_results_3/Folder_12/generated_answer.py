import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 45):
        for j in range(cols - 45):
            submatrix = matrix[i:i + 46, j:j + 46]
            if submatrix.size == 46:
                count += 1
    return count