import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 73
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if np.sum(submatrix == 73) == n:
                count += 1
    return count