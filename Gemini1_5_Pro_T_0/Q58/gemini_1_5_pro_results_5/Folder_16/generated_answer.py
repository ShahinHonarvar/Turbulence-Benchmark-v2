import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 153):
        for j in range(cols - 153):
            submatrix = matrix[i:i + 154, j:j + 154]
            if len(submatrix) * len(submatrix[0]) == 154:
                count += 1
    return count