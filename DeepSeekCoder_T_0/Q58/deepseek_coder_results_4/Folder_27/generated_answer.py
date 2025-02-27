import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows - 6):
        for c in range(cols - 6):
            submatrix = matrix[r:r + 7, c:c + 7]
            if np.size(submatrix) == 49 and np.all(submatrix == 77):
                count += 1
    return count