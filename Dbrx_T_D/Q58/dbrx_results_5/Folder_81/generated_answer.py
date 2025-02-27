import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0] - (matrix.shape[0] - i) % n + 1):
                for l in range(j, matrix.shape[1] - (matrix.shape[1] - j) % n + 1):
                    if (k - i + 1) * (l - j + 1) == n:
                        if np.all(matrix[i:k + 1, j:l + 1] == 97):
                            count += 1
    return count