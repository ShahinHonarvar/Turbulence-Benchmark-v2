import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix = np.array(matrix)
    n = 121
    rows, cols = matrix.shape
    min_dim = min(rows, cols)
    if min_dim < int(np.sqrt(n)) + 1:
        return 0
    for i in range(rows - min_dim + 1):
        for j in range(cols - min_dim + 1):
            if sum(matrix[i:i + min_dim, j:j + min_dim].reshape(-1)) == n:
                count += 1
    return count