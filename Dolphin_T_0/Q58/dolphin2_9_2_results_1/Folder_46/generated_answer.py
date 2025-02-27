import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 144
    m, n = matrix.shape
    i, j, k, l = (0, 0, 1, 1)
    while l <= n and k + l <= m and (j + l <= n):
        if len(np.unique(matrix[i:k, j:l])) == 1 and len(np.unique(matrix[k, j:l])) == 0 and (len(np.unique(matrix[i:k, j])) == 0) and (len(np.unique(matrix[i:k, l - 1])) == 1) and (len(np.unique(matrix[k - 1, j:l])) == 0) and (len(np.unique(matrix[k, j - 1])) == 1) and (len(np.unique(matrix[k, l - 1])) == 1) and (len(np.unique(matrix[k - 1, l - 1])) == 1):
            return 1
        else:
            k += 1
            l += 1
            if k > m and l > n:
                i += 1
                j += 1
                k = i + 1
                l = j + 1
    return 0