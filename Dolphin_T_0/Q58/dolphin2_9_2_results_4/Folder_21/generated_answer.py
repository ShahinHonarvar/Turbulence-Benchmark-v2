import numpy as np

def submatrix_with_n_numbers(matrix):
    h, w = matrix.shape
    count = 0
    for i in range(h):
        for j in range(w):
            for h_ in range(i, h):
                for w_ in range(j, w):
                    if np.count_nonzero(matrix[i:h_ + 1, j:w_ + 1]) == 139:
                        count += 1
    return count