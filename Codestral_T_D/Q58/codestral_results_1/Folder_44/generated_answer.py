import numpy as np

def submatrix_with_n_numbers(matrix, n=191):
    submatrix_count = 0
    i_max, j_max = matrix.shape
    for i in range(i_max):
        for j in range(j_max):
            for k in range(i, i_max):
                for l in range(j, j_max):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == n:
                        submatrix_count += 1
    return submatrix_count