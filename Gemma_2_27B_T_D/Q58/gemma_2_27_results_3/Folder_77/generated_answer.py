import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 13):
        for j in range(cols - 13):
            submatrix = matrix[i:i + 14, j:j + 14]
            if np.size(submatrix) == 179:
                count += 1
    return count