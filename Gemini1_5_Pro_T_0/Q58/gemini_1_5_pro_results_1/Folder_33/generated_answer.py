import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 117):
        for j in range(cols - 117):
            submatrix = matrix[i:i + 118, j:j + 118]
            if np.size(submatrix) == 118:
                count += 1
    return count