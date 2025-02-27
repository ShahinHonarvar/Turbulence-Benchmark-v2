import numpy as np

def submatrix_with_n_numbers(matrix, n=144):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            for k in range(i, i + int(np.sqrt(n))):
                for l in range(j, j + int(np.sqrt(n))):
                    if np.prod(matrix[i:k + 1, j:l + 1].shape) == n:
                        count += 1
    return count