import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape[0]
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 53:
                for sub_matrix in np.lib.stride_tritis.sliding_window(matrix[i:, j:], (53, 53), 'all'):
                    if sub_matrix.size == 53:
                        count += 1
    return count