import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    np.array(matrix)
    m = len(matrix)
    n = len(matrix[0])
    for i in range(0, m):
        for j in range(0, n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    if len(matrix[i:k + 1][j:l + 1].flatten()) == 57:
                        count += 1
    return count