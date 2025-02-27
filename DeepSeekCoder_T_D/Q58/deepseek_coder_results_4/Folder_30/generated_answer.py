import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            submatrix = matrix[r:r + 3, c:c + 3]
            if np.size(submatrix) == 9:
                if np.count_nonzero(submatrix == 94) == 9:
                    count += 1
    return count