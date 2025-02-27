import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 34
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n // rows < rows and j + n // cols < cols:
                if np.sum(matrix[i:i + n // rows, j:j + n // cols]) == n:
                    submatrix_count += 1
    return submatrix_count