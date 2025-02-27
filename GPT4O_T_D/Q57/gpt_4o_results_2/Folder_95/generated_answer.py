import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m, n, r, c):
        return [matrix[i:r, j:c] for i in range(m) for j in range(n) if i < r and j < c]

    def calculate_sum_of_submatrix(submatrix):
        return np.sum(submatrix)
    m, n = matrix.shape
    result = []
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            submatrices = get_submatrices(m, n, r, c)
            for submatrix in submatrices:
                if calculate_sum_of_submatrix(submatrix) == 19:
                    result.append(submatrix.tolist())
    return result