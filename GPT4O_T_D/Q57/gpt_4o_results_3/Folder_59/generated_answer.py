import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for r_start in range(rows):
            for c_start in range(cols):
                for r_end in range(r_start + 1, rows + 1):
                    for c_end in range(c_start + 1, cols + 1):
                        submatrix = mat[r_start:r_end, c_start:c_end]
                        if np.sum(submatrix) == 2:
                            submatrices.append(submatrix.tolist())
        return submatrices
    return find_submatrices(matrix)