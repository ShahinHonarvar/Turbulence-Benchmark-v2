import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix == 95) == size * size:
                    count += 1
    return count