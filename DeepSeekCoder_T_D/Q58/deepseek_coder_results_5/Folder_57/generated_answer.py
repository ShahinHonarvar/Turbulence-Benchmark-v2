import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 1):
        for c in range(cols - 1):
            submatrix = matrix[r:r + 2, c:c + 2]
            if np.size(submatrix) == 4 and np.count_nonzero(submatrix == 92) == 4:
                count += 1
    return count