import numpy as np
from scipy.ndimage import label, sum

def submatrix_with_n_numbers(matrix, n=118):
    s = matrix.shape
    H, W = (s[0] - 2, s[1] - 2)
    M, N = matrix.shape
    count = 0
    for h in range(H):
        for w in range(W):
            sub_matrix = matrix[h:h + 3, w:w + 3]
            if np.sum(sub_matrix) == n:
                count += 1
    return count