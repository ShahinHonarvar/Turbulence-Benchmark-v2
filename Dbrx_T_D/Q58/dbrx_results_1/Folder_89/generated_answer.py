import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(mat, n):
        if mat.shape[0] < n or mat.shape[1] < n:
            return 0
        count = 0
        for i in range(mat.shape[0] - n + 1):
            for j in range(mat.shape[1] - n + 1):
                submat = mat[i:i + n, j:j + n]
                if np.count_nonzero(submat) == n ** 2:
                    count += 1
        return count
    return count_submatrices(matrix, 18)