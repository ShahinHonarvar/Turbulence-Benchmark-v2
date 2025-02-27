import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 126):
        for j in range(cols - 126):
            submatrix = matrix[i:i + 127, j:j + 127]
            if np.sum(submatrix) == 127:
                count += 1
    return count