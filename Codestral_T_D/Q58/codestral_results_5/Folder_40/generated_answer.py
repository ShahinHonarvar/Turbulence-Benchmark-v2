import numpy as np

def submatrix_with_n_numbers(matrix, n=1):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix == n) == (k - i + 1) * (l - j + 1):
                        count += 1
    return count