import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            if len(np.unique(matrix[i:i + 2, j:j + 2])) == 2:
                count += 1
    return count