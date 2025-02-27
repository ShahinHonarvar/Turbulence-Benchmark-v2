import numpy as np

def submatrix_with_n_numbers(mat):
    row_len, col_len = mat.shape
    counter = 0
    for i in range(row_len - 2):
        for j in range(col_len - 2):
            submat = mat[i:i + 3, j:j + 3]
            if np.count_nonzero(submat == 37) == 9:
                counter += 1
    return counter