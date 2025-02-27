import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 40):
        for j in range(cols - 40):
            submatrix = matrix[i:i + 41, j:j + 41]
            if np.size(submatrix) == 41:
                count += 1
    return count