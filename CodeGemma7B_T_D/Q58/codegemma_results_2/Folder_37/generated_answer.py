import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k + 1, matrix.shape[1]):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if submatrix.shape[0] * submatrix.shape[1] == 64 and submatrix.size == np.unique(submatrix).size:
                        count += 1
    return count