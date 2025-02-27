import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for left in range(m):
        for right in range(left, m):
            for top in range(n):
                for down in range(top, n):
                    submatrix_sum = np.sum(matrix[top:down + 1, left:right + 1])
                    if submatrix_sum == 84:
                        submatrices.append(matrix[top:down + 1, left:right + 1])
    return submatrices