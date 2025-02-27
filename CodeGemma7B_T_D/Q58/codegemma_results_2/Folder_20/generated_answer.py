import numpy as np

def submatrix_with_n_numbers(matrix):
    x = np.cumsum(matrix, axis=0)
    y = np.cumsum(x, axis=1)
    z = y[:, :-48]
    count = 0
    for i in range(48):
        for j in range(matrix.shape[1] - i):
            if z[i + j, j] - z[i, j] - z[i + j, j + 49] + z[i, j + 49] == 49:
                count += 1
    return count