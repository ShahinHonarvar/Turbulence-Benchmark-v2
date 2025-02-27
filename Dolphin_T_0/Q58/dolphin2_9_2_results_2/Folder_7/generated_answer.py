import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    if m * n < 121:
        return 0
    else:
        count = 0
        for i in range(m - 10):
            for j in range(n - 10):
                temp_matrix = matrix[i:i + 11, j:j + 11]
                if np.count_nonzero(temp_matrix == 121) == 121:
                    count += 1
        return count