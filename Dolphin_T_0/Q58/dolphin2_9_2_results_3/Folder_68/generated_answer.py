import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    for i in range(mat.shape[0] - 8):
        for j in range(mat.shape[1] - 8):
            if np.all(mat[i:i + 9, j:j + 9] == 74):
                count += 1
    return count