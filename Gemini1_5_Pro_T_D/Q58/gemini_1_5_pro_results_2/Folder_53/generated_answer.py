import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 23):
        for j in range(cols - 23):
            submatrix = matrix[i:i + 24, j:j + 24]
            if np.size(submatrix) == 576:
                count += 1
    return count