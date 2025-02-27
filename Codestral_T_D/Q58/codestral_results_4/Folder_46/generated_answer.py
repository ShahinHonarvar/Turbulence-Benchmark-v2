import numpy as np

def submatrix_with_n_numbers(matrix, n=144):
    row, col = matrix.shape
    count = 0
    for i in range(row - int(np.sqrt(n)) + 1):
        for j in range(col - int(np.sqrt(n)) + 1):
            for k in range(i + int(np.sqrt(n))):
                for l in range(j + int(np.sqrt(n))):
                    if np.prod(matrix[i:k + 1, j:l + 1].shape) == n:
                        count += 1
    return count