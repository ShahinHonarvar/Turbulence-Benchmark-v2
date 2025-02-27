import numpy as np

def get_all_submatrices(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    submatrix = matrix[r:r2 + 1, c:c2 + 1]
                    submatrices.append(submatrix)
    return submatrices

def submatrix_with_particular_sum(matrix):
    submatrices = get_all_submatrices(matrix)
    result = []
    for submatrix in submatrices:
        if np.sum(submatrix) == -83:
            result.append(submatrix.tolist())
    return result