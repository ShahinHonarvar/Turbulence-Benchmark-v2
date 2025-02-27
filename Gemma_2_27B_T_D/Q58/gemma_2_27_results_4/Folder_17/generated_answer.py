import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 166
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + np.sqrt(n).astype(int) <= matrix.shape[0] and j + np.sqrt(n).astype(int) <= matrix.shape[1]:
                submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
                if submatrix.size == n:
                    count += 1
    return count