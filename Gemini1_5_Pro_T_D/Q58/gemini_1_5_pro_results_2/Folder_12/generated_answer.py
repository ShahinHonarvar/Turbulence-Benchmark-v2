import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 5):
        for j in range(cols - 5):
            submatrix = matrix[i:i + 6, j:j + 6]
            if np.size(submatrix) == 46:
                count += 1
    return count