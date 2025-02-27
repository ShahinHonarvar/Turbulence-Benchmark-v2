import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 63
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + int(np.sqrt(n)) - 1 < rows and j + int(np.sqrt(n)) - 1 < cols:
                submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
                if submatrix.size == n:
                    count += 1
    return count