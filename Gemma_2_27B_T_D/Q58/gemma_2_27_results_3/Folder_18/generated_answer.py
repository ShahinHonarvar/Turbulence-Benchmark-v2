import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 10):
        for j in range(cols - 10):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.size(submatrix) == 104:
                count += 1
    return count