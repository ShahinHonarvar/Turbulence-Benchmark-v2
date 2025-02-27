import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_submatrix(matrix, submatrix):
        m, n = (len(matrix), len(matrix[0]))
        p, q = (len(submatrix), len(submatrix[0]))
        for i in range(m - p + 1):
            for j in range(n - q + 1):
                if (matrix[i:i + p, j:j + q] == submatrix).all():
                    return True
        return False

    def check_sum(submatrix):
        return np.sum(submatrix) == -452
    m, n = (len(matrix), len(matrix[0]))
    submatrices = []
    for p in range(1, m + 1):
        for q in range(1, n + 1):
            for i in range(m - p + 1):
                for j in range(n - q + 1):
                    submatrix = matrix[i:i + p, j:j + q]
                    if is_submatrix(matrix, submatrix) and check_sum(submatrix):
                        submatrices.append(submatrix)
    return submatrices