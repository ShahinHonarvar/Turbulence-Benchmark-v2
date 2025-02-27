import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 22):
        for j in range(cols - 22):
            submatrix = matrix[i:i + 23, j:j + 23]
            if np.size(submatrix) == 23 * 23:
                count += 1
    return count