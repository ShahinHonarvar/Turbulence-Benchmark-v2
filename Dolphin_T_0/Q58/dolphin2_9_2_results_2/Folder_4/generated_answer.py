import numpy as np

def submatrix_with_n_numbers(matrix, n=15):
    row_num, col_num = matrix.shape
    counter = 0
    for i in range(row_num - n + 1):
        for j in range(col_num - n + 1):
            temp = matrix[i:i + n, j:j + n].flatten()
            if np.all(temp == n):
                counter += 1
    return counter