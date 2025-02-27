import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 79):
        for j in range(cols - 79):
            submatrix = matrix[i:i + 80, j:j + 80]
            if np.size(submatrix) == 6400:
                count += 1
    return count