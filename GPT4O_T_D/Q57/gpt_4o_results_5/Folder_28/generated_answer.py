import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, top, left, bottom, right):
        return np.sum(mat[top:bottom + 1, left:right + 1])

    def generate_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        submatrices.append((top, left, bottom, right))
        return submatrices
    submatrices = generate_submatrices(matrix)
    result = [matrix[top:bottom + 1, left:right + 1].tolist() for top, left, bottom, right in submatrices if submatrix_sum(matrix, top, left, bottom, right) == 15]
    return result