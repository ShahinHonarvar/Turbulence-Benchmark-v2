import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        num_rows, num_cols = mat.shape
        results = []
        for r1 in range(num_rows):
            for r2 in range(r1, num_rows):
                for c1 in range(num_cols):
                    for c2 in range(c1, num_cols):
                        submatrix = mat[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(submatrix) == target_sum:
                            results.append(submatrix.tolist())
        return results
    return find_submatrices_with_sum(matrix, -42)