import numpy as np

def submatrix_with_n_numbers(matrix):
    row_num, col_num = matrix.shape
    count = 0
    for i in range(row_num - 2):
        for j in range(col_num - 2):
            if np.prod(matrix[i:i + 3, j:j + 3]) == 10:
                count += 1
    return count