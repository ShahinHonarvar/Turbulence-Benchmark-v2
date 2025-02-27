import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix, n=78):
    rows, cols = matrix.shape
    submatrices = np.array([matrix[i:j, k:l] for i in range(rows) for j in range(i + 1, rows + 1) for k in range(cols) for l in range(k + 1, cols + 1)])
    counts = [np.sum(submatrix == 78) for submatrix in submatrices]
    return len([count for count in counts if count == n])