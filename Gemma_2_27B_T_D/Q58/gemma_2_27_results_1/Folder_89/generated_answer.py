import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 18
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.floor(np.sqrt(n))) + 1):
        for j in range(cols - int(np.floor(np.sqrt(n))) + 1):
            submatrix = matrix[i:i + int(np.floor(np.sqrt(n))), j:j + int(np.floor(np.sqrt(n)))]
            if submatrix.size == n:
                count += 1
    return count