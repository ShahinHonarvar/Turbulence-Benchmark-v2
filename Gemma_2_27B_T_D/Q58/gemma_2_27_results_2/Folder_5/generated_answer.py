import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 63
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if submatrix.size == n:
                count += 1
    return count