import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(m - 2):
        for j in range(n - 2):
            for k in range(i + 3, m + 1):
                for l in range(j + 3, n + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 97:
                        count += 1
    return count