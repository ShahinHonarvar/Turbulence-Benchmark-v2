import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_with_sum(n, m):
        result = []
        for r1 in range(n):
            for r2 in range(r1, n):
                for c1 in range(m):
                    for c2 in range(c1, m):
                        sub_matrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(sub_matrix) == 92:
                            result.append(sub_matrix.tolist())
        return result
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return []
    rows, cols = matrix.shape
    return get_submatrices_with_sum(rows, cols)