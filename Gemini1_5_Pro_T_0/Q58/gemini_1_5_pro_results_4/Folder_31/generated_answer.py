import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 44):
        for j in range(cols - 44):
            submatrix = matrix[i:i + 45, j:j + 45]
            if np.size(submatrix) == 45:
                count += 1
    return count