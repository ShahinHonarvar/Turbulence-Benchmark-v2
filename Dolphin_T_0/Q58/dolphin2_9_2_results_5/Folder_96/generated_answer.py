import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    matrix = np.array(matrix)
    count = 0
    for i in range(m - 1):
        for j in range(n - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if len(submatrix.flatten()) == 20:
                count += 1
    return count