import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for top in range(m):
        for left in range(n):
            for bottom in range(top, m):
                for right in range(left, n):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == 77:
                        result.append(submatrix)
    return result