import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 120
    matrix_size = matrix.shape[0] * matrix.shape[1]
    if submatrix_size > matrix_size:
        return 0
    count = 0
    for i in range(matrix.shape[0] - int(np.sqrt(submatrix_size)) + 1):
        for j in range(matrix.shape[1] - int(np.sqrt(submatrix_size)) + 1):
            for k in range(int(np.sqrt(submatrix_size))):
                for l in range(int(np.sqrt(submatrix_size))):
                    if np.sum(matrix[i:i + k + 1, j:j + l + 1]) == 120:
                        count += 1
    return count