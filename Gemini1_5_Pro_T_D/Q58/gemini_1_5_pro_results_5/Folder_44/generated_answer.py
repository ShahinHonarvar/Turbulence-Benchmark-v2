import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 190):
        for j in range(cols - 190):
            submatrix = matrix[i:i + 191, j:j + 191]
            if np.size(submatrix) == 191:
                count += 1
    return count