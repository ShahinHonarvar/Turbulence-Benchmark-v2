import numpy as np

def submatrix_with_n_numbers(matrix):
    row_length, col_length = matrix.shape
    count = 0
    for i in range(row_length):
        for j in range(col_length):
            if matrix[i, j] == 29:
                if np.all([matrix[i:i + 2, j:j + 2] == 29]):
                    count += 1
    if count > 0:
        return count
    else:
        return 0