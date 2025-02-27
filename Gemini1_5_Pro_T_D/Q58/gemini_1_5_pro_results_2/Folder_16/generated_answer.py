import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 14):
        for j in range(cols - 13):
            submatrix = matrix[i:i + 15, j:j + 14]
            if np.size(submatrix) == 154:
                count += 1
    return count