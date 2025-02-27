import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    n, m = matrix.shape
    result = []
    for top in range(n):
        for left in range(m):
            for bottom in range(top, n):
                for right in range(left, m):
                    if submatrix_sum(matrix, top, left, bottom, right) == -13:
                        submatrix = matrix[top:bottom + 1, left:right + 1].tolist()
                        result.append(submatrix)
    return result