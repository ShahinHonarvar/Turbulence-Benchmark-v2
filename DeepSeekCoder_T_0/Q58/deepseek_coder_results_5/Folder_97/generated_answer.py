import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 119):
        for j in range(cols - 119):
            if np.size(matrix[i:i + 120, j:j + 120]) == 14400:
                count += 1
    return count