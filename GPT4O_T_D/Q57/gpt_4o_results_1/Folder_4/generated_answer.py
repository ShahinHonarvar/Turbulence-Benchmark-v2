import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(mat, top, left, bottom, right):
        return np.sum(mat[top:bottom + 1, left:right + 1])

    def find_submatrices(mat, target_sum):
        rows, cols = mat.shape
        matching_submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        if get_submatrix_sum(mat, top, left, bottom, right) == target_sum:
                            submatrix = mat[top:bottom + 1, left:right + 1].tolist()
                            matching_submatrices.append(submatrix)
        return matching_submatrices
    return find_submatrices(matrix, 87)