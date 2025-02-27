import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    cnt = 0
    for i in range(m - 1):
        for j in range(n - 1):
            element_count = matrix[i:i + 2, j:j + 2].sum()
            if element_count == 179:
                cnt += 1
    return cnt