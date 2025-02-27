import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        n, m = matrix.shape
        for i in range(n):
            for j in range(m):
                for k in range(i + 1, n + 1):
                    for l in range(j + 1, m + 1):
                        if matrix[i:k, j:l].sum() == 21:
                            yield matrix[i:k, j:l]
    return list(get_submatrices(matrix))