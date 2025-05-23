import numpy as np

def submatrix_with_n_numbers(matrix, n=1):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.count_nonzero(submatrix == n) == submatrix.size:
                        count += 1
    return count