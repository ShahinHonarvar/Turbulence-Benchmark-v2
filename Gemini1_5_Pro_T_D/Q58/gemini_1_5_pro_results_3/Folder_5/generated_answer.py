import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 6 + 1):
        for j in range(cols - 3 + 1):
            submatrix = matrix[i:i + 6, j:j + 3]
            if np.size(submatrix) == 63:
                count += 1
    return count