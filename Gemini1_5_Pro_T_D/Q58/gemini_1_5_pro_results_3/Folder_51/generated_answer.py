import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 95 + 1):
        for j in range(cols - 95 + 1):
            submatrix = matrix[i:i + 95, j:j + 95]
            if np.size(submatrix) == 95:
                count += 1
    return count