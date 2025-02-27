import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for p in range(i, n):
                for q in range(j, m):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if np.count_nonzero(submatrix == 1) == 1:
                        count += 1
    return count