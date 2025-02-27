import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    matrix = np.array(matrix)
    for i in range(m - 1):
        for j in range(n - 1):
            top_left_elements = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
            if 43 in top_left_elements:
                count += 1
    return count