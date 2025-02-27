import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 28):
        for j in range(cols - 28):
            submatrix = matrix[i:i + 29, j:j + 29]
            if np.size(submatrix) == 29 * 29:
                count += 1
    return count