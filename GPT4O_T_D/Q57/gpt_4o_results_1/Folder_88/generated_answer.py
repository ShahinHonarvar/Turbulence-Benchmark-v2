import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    m, n = matrix.shape
    result = []
    for top in range(m):
        for left in range(n):
            for bottom in range(top, m):
                for right in range(left, n):
                    if get_submatrix_sum(top, left, bottom, right) == -64:
                        submatrix = matrix[top:bottom + 1, left:right + 1].tolist()
                        result.append(submatrix)
    return result