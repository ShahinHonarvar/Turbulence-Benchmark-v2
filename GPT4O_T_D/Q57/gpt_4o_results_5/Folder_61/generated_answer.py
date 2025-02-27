import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(target_sum):
        rows, cols = matrix.shape
        result = []
        for i in range(rows):
            for j in range(cols):
                for h in range(i, rows):
                    for k in range(j, cols):
                        submatrix = matrix[i:h + 1, j:k + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix.tolist())
        return result
    return find_submatrices_with_sum(8)