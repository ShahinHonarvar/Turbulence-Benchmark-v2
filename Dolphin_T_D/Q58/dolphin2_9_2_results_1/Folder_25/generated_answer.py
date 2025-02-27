import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape
    count = 0
    for i in range(size[0]):
        for j in range(size[1]):
            for k in range(i + 1, size[0]):
                for l in range(j + 1, size[1]):
                    submatrix = matrix[i:k, j:l]
                    if np.count_nonzero(submatrix) == 66:
                        count += 1
    return count