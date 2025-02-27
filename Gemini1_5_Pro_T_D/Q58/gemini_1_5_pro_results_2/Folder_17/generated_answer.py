import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 15):
        for j in range(cols - 15):
            submatrix = matrix[i:i + 16, j:j + 16]
            if np.size(submatrix) == 166:
                count += 1
    return count