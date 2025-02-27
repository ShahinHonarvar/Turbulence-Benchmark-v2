import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 178):
        for j in range(cols - 178):
            submatrix = matrix[i:i + 179, j:j + 179]
            if np.prod(submatrix.shape) == 179:
                count += 1
    return count