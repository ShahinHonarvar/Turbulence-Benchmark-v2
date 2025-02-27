import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    s = matrix.shape
    for i in range(s[0]):
        for j in range(s[1]):
            for k in range(i, s[0]):
                for l in range(j, s[1]):
                    if len(np.unique(matrix[i:k + 1, j:l + 1])) == 35:
                        count += 1
    return count