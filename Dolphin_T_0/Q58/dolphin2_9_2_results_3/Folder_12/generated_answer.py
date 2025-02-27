import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            if matrix[i, j] == 46:
                for k in range(i + 1, matrix_size[0]):
                    for l in range(j + 1, matrix_size[1]):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.count_nonzero(submatrix == 46) == 46:
                            count += 1
    return count