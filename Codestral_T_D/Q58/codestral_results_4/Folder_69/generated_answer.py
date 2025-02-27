import numpy as np

def submatrix_with_n_numbers(matrix, n=126):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    submatrices.append(matrix[r:i + 1, c:j + 1])
    count = sum((np.prod(submatrix.shape) == n for submatrix in submatrices))
    return count