import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 1):
        for col in range(cols - 1):
            submatrix = matrix[row:, col:]
            if submatrix.shape[0] * submatrix.shape[1] >= 104 and np.count_nonzero(submatrix == 104) == 104:
                count += 1
    return count