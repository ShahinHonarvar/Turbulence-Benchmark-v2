import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_with_sum = []
    rows, cols = matrix.shape
    for i in range(rows + 1):
        for j in range(cols + 1):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -97:
                        submatrices_with_sum.append(submatrix)
    if len(submatrices_with_sum) == 0:
        return []
    else:
        return submatrices_with_sum