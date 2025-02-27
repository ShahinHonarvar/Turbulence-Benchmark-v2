import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 52):
        for j in range(cols - 52):
            submatrix = matrix[i:i + 53, j:j + 53]
            if np.size(submatrix) == 53:
                count += 1
    return count