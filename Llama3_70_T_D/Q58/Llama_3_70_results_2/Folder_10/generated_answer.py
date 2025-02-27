import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = matrix.shape[0] * matrix.shape[1] // 56
    if n == 0:
        return 0
    for i in range(matrix.shape[0] - int(np.sqrt(n)) + 1):
        for j in range(matrix.shape[1] - int(np.sqrt(n)) + 1):
            for k in range(i + int(np.sqrt(n)), matrix.shape[0] + 1):
                for l in range(j + int(np.sqrt(n)), matrix.shape[1] + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 56:
                        count += 1
    return count