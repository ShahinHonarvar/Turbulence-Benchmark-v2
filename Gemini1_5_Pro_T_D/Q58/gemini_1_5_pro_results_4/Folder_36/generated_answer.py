import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 12):
        for j in range(cols - 12):
            submatrix = matrix[i:i + 13, j:j + 13]
            if np.size(submatrix) == 131:
                count += 1
    return count