import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r + 1, rows + 1):
                for c_end in range(c + 1, cols + 1):
                    submatrix = matrix[r:r_end, c:c_end]
                    if np.sum(submatrix) == -65:
                        result.append(submatrix.tolist())
    return result