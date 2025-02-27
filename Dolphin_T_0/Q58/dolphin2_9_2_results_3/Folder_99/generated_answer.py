import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 13):
        for j in range(cols - 13):
            if np.count_nonzero(matrix[i:i + 146, j:j + 146]) == 146:
                count += 1
    return count * (rows - 13) * (cols - 13)