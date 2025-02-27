import numpy as np
from numpy.lib.arraysetops import in1d

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    indices = np.arange(rows * cols).reshape(rows, cols)
    submatrix_indices = []
    for i in range(1, min(rows, cols) + 1):
        for j in range(cols - i + 1):
            for k in range(rows - i + 1):
                submatrix = matrix[k:k + i, j:j + i]
                if np.sum(submatrix) == 186:
                    count += 1
    return count