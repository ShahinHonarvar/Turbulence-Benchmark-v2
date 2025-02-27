import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 26):
        for j in range(cols - 26):
            submatrix = matrix[i:i + 27, j:j + 27]
            if len(submatrix) * len(submatrix[0]) == 27:
                count += 1
    return count