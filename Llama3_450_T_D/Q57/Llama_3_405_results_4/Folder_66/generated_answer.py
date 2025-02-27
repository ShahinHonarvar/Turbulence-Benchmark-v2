import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(matrix):
        submatrices = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                for k in range(i, matrix.shape[0]):
                    for end_col in range(j, matrix.shape[1]):
                        submatrices.append(matrix[i:k + 1, j:end_col + 1])
        return submatrices
    return [submatrix for submatrix in get_all_submatrices(matrix) if np.sum(submatrix) == 99]