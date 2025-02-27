import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        m, n = matrix.shape
        for top in range(m):
            for left in range(n):
                for bottom in range(top, m):
                    for right in range(left, n):
                        yield matrix[top:bottom + 1, left:right + 1]
    result = []
    for submatrix in get_submatrices(matrix):
        if np.sum(submatrix) == 95:
            result.append(submatrix.tolist())
    return result