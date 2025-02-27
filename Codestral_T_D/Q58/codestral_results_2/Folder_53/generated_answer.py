import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 24
    count = 0
    if rows < np.sqrt(n) or cols < np.sqrt(n):
        return 0
    for i in range(rows - np.sqrt(n) + 1):
        for j in range(cols - np.sqrt(n) + 1):
            submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if submatrix.size == n:
                count += 1
    return count