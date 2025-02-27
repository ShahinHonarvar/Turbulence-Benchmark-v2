import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 8):
        for j in range(cols - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.size(submatrix) == 92:
                count += 1
    return count