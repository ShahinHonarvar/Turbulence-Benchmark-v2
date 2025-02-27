import numpy as np

def submatrix_with_n_numbers(matrix):
    if np.count_nonzero(matrix == 95) == 0:
        return 0
    else:
        submatrices = 0
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i, j] == 95:
                    submatrices += 1
                    for size in range(2, min(matrix.shape[0] - i + 1, matrix.shape[1] - j + 1) + 1):
                        submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                        if submatrix_sum == 95:
                            submatrices += 1
        return submatrices