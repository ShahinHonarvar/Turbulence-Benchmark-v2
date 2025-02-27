import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(start_row, start_col, target_sum):
        submatrices = []
        for end_row in range(start_row, n):
            for end_col in range(start_col, m):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                if np.sum(submatrix) == target_sum:
                    submatrices.append(submatrix.tolist())
        return submatrices
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            result.extend(find_submatrices_with_sum(i, j, 66))
    return result