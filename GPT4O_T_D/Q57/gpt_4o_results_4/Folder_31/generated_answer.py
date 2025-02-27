import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrices.append(mat[i:k, j:l])
        return submatrices
    all_submatrices = get_submatrices(matrix)
    result = []
    for submatrix in all_submatrices:
        if np.sum(submatrix) == -44:
            result.append(submatrix)
    return result