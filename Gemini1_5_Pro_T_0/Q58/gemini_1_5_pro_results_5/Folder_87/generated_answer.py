import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 7):
        for j in range(cols - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.size(submatrix) == 96:
                count += 1
    return count